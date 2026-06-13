# ============================================================
#  services/pdf_service.py — PDF text extraction
#  Responsible for: reading a PDF binary and returning clean text.
#  Uses PyMuPDF (imported as fitz).
# ============================================================

import re
import fitz   # PyMuPDF


def extract_text(pdf_file) -> str:
    """
    Accepts a file-like object (from Flask's request.files),
    reads all pages, and returns the full text as a single string.

    Why PyMuPDF?
      - Handles multi-column layouts better than pdfminer
      - Faster and more reliable for standard resume PDFs
      - fitz.open(stream=...) lets us read from memory without saving to disk
    """
    pdf_bytes = pdf_file.read()

    # Open from bytes — no need to save the file to disk first
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Collapse 3+ consecutive newlines into 2 (clean up spacing)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()
