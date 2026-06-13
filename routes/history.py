# ============================================================
#  routes/history.py — GET /history
#  Returns the last 20 match results from MongoDB.
# ============================================================

from flask import Blueprint, jsonify
from db.mongo import collection

history_bp = Blueprint('history', __name__)


@history_bp.route('/history', methods=['GET'])
def get_history():
    """
    Fetches the 20 most recent match records from MongoDB,
    sorted by matched_at descending (newest first).

    _id is excluded because MongoDB's ObjectId is not
    JSON-serializable by default — it would cause a crash.

    matched_at (a Python datetime) is converted to a string
    so React can display it without any extra parsing.
    """
    cursor = (
        collection
        .find({}, {"_id": 0})          # exclude _id field
        .sort("matched_at", -1)        # -1 = descending (newest first)
        .limit(20)
    )

    rows = []
    for doc in cursor:
        # Convert datetime object → readable string for the frontend
        doc["matched_at"] = doc["matched_at"].strftime("%Y-%m-%d %H:%M:%S")
        rows.append(doc)

    return jsonify({"history": rows})
