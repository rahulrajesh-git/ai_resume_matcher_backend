# AI Resume Matcher

A full stack web application that scores how well a resume matches a job description using **BERT-based semantic similarity** — going beyond simple keyword matching to understand the actual meaning of the text.

---

## Features

- **PDF resume upload** with drag-and-drop support
- **Semantic match scoring (0–100%)** using BERT embeddings and cosine similarity
- **Keyword gap analysis** — highlights job description terms missing from the resume
- **Match history** — stores and displays the last 20 analyses
- **Animated score visualization** with color-coded results

---

## Tech Stack

**Frontend**
- React (Hooks, Fetch API, FormData, SVG)

**Backend**
- Python, Flask (Blueprints, REST API)
- flask-cors, python-dotenv

**AI / NLP**
- `sentence-transformers` (`all-MiniLM-L6-v2` BERT model)
- `scikit-learn` (cosine similarity)

**PDF Parsing**
- PyMuPDF (`fitz`) — in-memory text extraction

**Database**
- MongoDB (`pymongo`)

---

## How It Works

1. User uploads a resume PDF and pastes a job description in the React frontend.
2. Flask extracts raw text from the PDF using PyMuPDF.
3. BERT (`sentence-transformers`) encodes both the resume and job description into 384-dimensional vectors.
4. Cosine similarity between the two vectors produces a match score (0–100%).
5. Missing keywords are identified via set subtraction between the job description and resume text.
6. The result is saved to MongoDB and returned to the frontend, which displays the score, missing keywords, and match history.

---

## Project Structure

```
ai-resume-matcher/
├── app.py                  # Entry point — creates and runs the Flask app
├── config.py               # Centralized environment variable configuration
├── requirements.txt
├── .env                     # Environment variables (not committed)
│
├── routes/
│   ├── match.py             # POST /match
│   └── history.py           # GET /history
│
├── services/
│   ├── bert_service.py      # BERT model loading + cosine similarity
│   ├── pdf_service.py        # PDF text extraction
│   └── keyword_service.py   # Missing keyword analysis
│
├── db/
│   └── mongo.py             # MongoDB connection
│
└── resume-matcher-frontend/
    └── src/
        └── App.js           # React frontend
```

---

## Setup & Installation

### Prerequisites
- Python 3.9+
- Node.js & npm
- MongoDB installed and running locally

### Backend

```bash
# Clone the repo
git clone https://github.com/<your-username>/ai-resume-matcher.git
cd ai-resume-matcher

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Create a .env file
echo MONGO_URI=mongodb://localhost:27017/ > .env
echo MONGO_DB=resume_matcher >> .env
echo BERT_MODEL=all-MiniLM-L6-v2 >> .env

# Start MongoDB (in a separate terminal)
mongod

# Run the Flask server
python app.py
```

The backend runs on `http://localhost:5000`.

### Frontend

```bash
cd resume-matcher-frontend
npm install
npm start
```

The frontend runs on `http://localhost:3000`.

---

## API Endpoints

| Method | Endpoint    | Description                                  |
|--------|-------------|-----------------------------------------------|
| POST   | `/match`    | Accepts a resume PDF + job description, returns match score and missing keywords |
| GET    | `/history`  | Returns the last 20 match results |
| GET    | `/health`   | Health check endpoint |

---

## Architecture Notes

- **Separation of concerns** — routes handle HTTP only, services contain all business logic, and the database layer is isolated.
- **BERT model loaded once at startup** to avoid reloading ~90MB of model weights on every request.
- **Environment-based configuration** via `.env` and `config.py` — no hardcoded secrets.
- **CORS enabled** between the React frontend (port 3000) and Flask backend (port 5000).

---

## Future Improvements

- User authentication for tracking multiple job applications
- Docker-based deployment for the full stack
- Section-level scoring (skills, experience, education scored separately)
- Job description scraping from job boards