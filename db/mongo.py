# ============================================================
#  db/mongo.py — MongoDB connection
#  Single MongoClient shared across the entire app.
#  Any file that needs the DB imports `collection` from here.
# ============================================================

from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB

# MongoClient is thread-safe — one instance is enough for the whole app.
# Creating a new connection per request would be slow and wasteful.
client     = MongoClient(MONGO_URI)
db         = client[MONGO_DB]

# The collection where all match results are stored.
# MongoDB creates it automatically on first insert — no setup needed.
collection = db["matches"]
