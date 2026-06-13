# ============================================================
#  services/bert_service.py — BERT model + similarity logic
#  Responsible for: loading the model, encoding text, scoring.
#  Nothing else. Routes don't touch this logic directly.
# ============================================================

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from config import BERT_MODEL

# Load once when this module is first imported (at app startup).
# If this were inside a function, the model would reload on every request — very slow.
print(f"Loading BERT model: {BERT_MODEL} ...")
_model = SentenceTransformer(BERT_MODEL)
print("BERT model ready.")


def get_match_score(resume_text: str, jd_text: str) -> float:
    """
    Encodes both texts into 384-dimensional vectors using BERT,
    then computes cosine similarity between them.

    Cosine similarity measures the angle between two vectors:
      - Score = 1.0  → identical meaning (angle = 0°)
      - Score = 0.0  → completely unrelated (angle = 90°)

    Returns a percentage (0.0 – 100.0), e.g. 78.5
    """
    # model.encode() returns a numpy array of shape (2, 384)
    embeddings = _model.encode([resume_text, jd_text])

    # cosine_similarity expects 2D arrays — hence the [[ ]] wrapping
    raw_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    # Multiply by 100 and round to 1 decimal place
    return round(float(raw_score) * 100, 1)
