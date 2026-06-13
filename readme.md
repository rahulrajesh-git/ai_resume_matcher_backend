# AI Resume Matcher

AI Resume Matcher is a web application that analyzes how well a candidate's resume matches a given Job Description (JD). The system uses Natural Language Processing (NLP) and BERT embeddings to calculate semantic similarity between resumes and job requirements. It also performs keyword gap analysis and stores match history for future reference.

## Features

* Upload resume in PDF format
* Enter or paste a Job Description
* Extract text from uploaded resumes
* Generate BERT-based semantic similarity scores
* Identify missing keywords from the Job Description
* Display overall match percentage
* Store previous match results in MongoDB
* View recent matching history
* Responsive React frontend

---

## Tech Stack

### Frontend

* React.js
* Axios
* CSS

### Backend

* Flask
* Flask-CORS

### AI / NLP

* Sentence Transformers (BERT)
* Scikit-learn

### Database

* MongoDB

### Other Libraries

* PyPDF2
* Python-dotenv

---

## Project Structure

### Backend

```text
airesumematcher/
│
├── app.py
├── config.py
├── .env
│
├── routes/
│   ├── match.py
│   └── history.py
│
├── services/
│   ├── pdf_service.py
│   ├── bert_service.py
│   └── keyword_service.py
│
└── db/
    └── mongo.py
```

### Frontend

```text
resumematcherfrontend/
│
├── src/
│   ├── App.js
│   ├── components/
│   └── services/
│
└── public/
```

---

## How It Works

1. User uploads a resume PDF.
2. The backend extracts text from the PDF.
3. The job description is received from the frontend.
4. BERT generates embeddings for both resume and JD.
5. Cosine similarity is calculated to determine match percentage.
6. Keyword analysis identifies missing skills or requirements.
7. Results are displayed on the frontend.
8. Match history is stored in MongoDB.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-resume-matcher.git
cd ai-resume-matcher
```

### Backend Setup

Create and activate virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string
```

Run Flask server:

```bash
python app.py
```

Backend runs on:

```text
http://localhost:5000
```

---

### Frontend Setup

Navigate to frontend folder:

```bash
cd resumematcherfrontend
```

Install dependencies:

```bash
npm install
```

Run React application:

```bash
npm start
```

Frontend runs on:

```text
http://localhost:3000
```

---

## API Endpoints

### Match Resume

```http
POST /match
```

Request:

* resume (PDF file)
* job_description (text)

Response:

```json
{
  "match_score": 85.6,
  "missing_keywords": [
    "Docker",
    "Kubernetes"
  ]
}
```

---

### Match History

```http
GET /history
```

Returns the most recent matching results stored in MongoDB.

---

## Sample Use Case

### Job Description

```text
Python Developer with Flask, MongoDB, Docker, and REST API experience.
```

### Resume Contains

```text
Python, Flask, MongoDB, REST APIs
```

### Output

```text
Match Score: 87%
Missing Keywords:
- Docker
```

---

## Future Enhancements

* Multi-resume comparison
* Skill recommendation system
* ATS score calculation
* Resume improvement suggestions
* Support for DOCX files
* User authentication and dashboards

---

## Author

Rahul

Final Year Engineering Student

AI Resume Matcher Project using Flask, React, BERT, and MongoDB.
