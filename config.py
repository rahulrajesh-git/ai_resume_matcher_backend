# ============================================================
#  config.py — All environment variables in one place
#  Import from here everywhere — never use os.getenv() directly
#  in routes or services. If a variable name changes, fix it here only.
# ============================================================

import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB  = os.getenv("MONGO_DB",  "resume_matcher")

BERT_MODEL = os.getenv("BERT_MODEL", "all-MiniLM-L6-v2")

FLASK_PORT  = int(os.getenv("FLASK_PORT", 5000))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
