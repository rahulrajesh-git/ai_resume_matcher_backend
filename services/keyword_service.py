# ============================================================
#  services/keyword_service.py — Keyword gap analysis
#  Responsible for: finding JD keywords missing from the resume.
# ============================================================

import re

# Common English words that add no signal — filter these out
# so results only show meaningful technical/domain terms.
STOP_WORDS = {
    "and", "the", "to", "of", "in", "a", "is", "for", "with",
    "you", "we", "are", "be", "as", "an", "on", "or", "at",
    "have", "will", "your", "our", "that", "this", "it", "by",
    "from", "not", "but", "can", "also", "which", "all", "more"
}


def find_missing_keywords(resume_text: str, jd_text: str) -> list:
    """
    Extracts all meaningful words (3+ characters) from the job description,
    then returns the ones not found anywhere in the resume.

    This is simple set subtraction — not NLP — so it's fast and explainable.
    Good enough to surface keywords like 'docker', 'agile', 'kubernetes'
    that the candidate forgot to include.

    Returns up to 10 missing keywords, sorted alphabetically.
    """
    # re.findall with \b[a-z]{3,}\b extracts whole lowercase words of 3+ chars
    jd_words     = set(re.findall(r'\b[a-z]{3,}\b', jd_text.lower()))
    resume_words = set(re.findall(r'\b[a-z]{3,}\b', resume_text.lower()))

    missing = jd_words - resume_words - STOP_WORDS

    return sorted(list(missing))[:10]
