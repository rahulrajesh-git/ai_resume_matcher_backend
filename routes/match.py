# ============================================================
#  routes/match.py — POST /match
#  Only job: validate the request, call services, return JSON.
#  Zero business logic lives here — that all lives in services/.
# ============================================================

from flask import Blueprint, request, jsonify
from datetime import datetime

from services.pdf_service     import extract_text
from services.bert_service    import get_match_score
from services.keyword_service import find_missing_keywords
from db.mongo                 import collection

# Blueprint lets us define routes in a separate file and register
# them in app.py — keeps the entry point clean.
match_bp = Blueprint('match', __name__)


@match_bp.route('/match', methods=['POST'])
def match_resume():
    """
    Expects multipart/form-data:
      - resume          : PDF file
      - job_description : plain text string

    Returns JSON:
      {
        "score": 78.5,
        "missing_keywords": ["docker", "agile"],
        "resume_length": 1204,
        "status": "success"
      }
    """

    # ── 1. Validate inputs ─────────────────────────────────────────────────
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    pdf_file = request.files['resume']
    jd_text  = request.form.get('job_description', '').strip()

    if pdf_file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    if not jd_text:
        return jsonify({"error": "Job description is required"}), 400

    # ── 2. Extract text from PDF (pdf_service) ─────────────────────────────
    try:
        resume_text = extract_text(pdf_file)
    except Exception as e:
        return jsonify({"error": f"Could not read PDF: {str(e)}"}), 422

    if len(resume_text) < 50:
        return jsonify({"error": "PDF appears empty or image-only (non-parseable)"}), 422

    # ── 3. Score with BERT (bert_service) ──────────────────────────────────
    score = get_match_score(resume_text, jd_text)

    # ── 4. Keyword gap (keyword_service) ───────────────────────────────────
    missing_keywords = find_missing_keywords(resume_text, jd_text)

    # ── 5. Persist to MongoDB ──────────────────────────────────────────────
    try:
        collection.insert_one({
            "resume_snip": resume_text[:300],
            "jd_snip":     jd_text[:300],
            "score":        score,
            "matched_at":  datetime.utcnow()
        })
    except Exception as e:
        # Don't crash the request if DB save fails — just log it
        print(f"[WARNING] MongoDB save failed: {e}")

    # ── 6. Return response ─────────────────────────────────────────────────
    return jsonify({
        "score":            score,
        "missing_keywords": missing_keywords,
        "resume_length":    len(resume_text),
        "status":           "success"
    })


@match_bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "model": "all-MiniLM-L6-v2", "db": "mongodb"})
