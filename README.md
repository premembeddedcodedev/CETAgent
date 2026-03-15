Here’s a README.md you can add to your project root. It documents setup, usage, and features step by step so anyone (including future you) can get the quiz system running quickly.

# Current Affairs Quiz Agent

An AI‑powered quiz generator that pulls facts from **NewsAPI**, **Google News RSS**, and **PDFs**, then uses Hugging Face models to generate natural questions and answers. Users can take quizzes via a Flask web app, track their answers, and retry wrong ones for reinforcement.

---

## 📂 Project Structure

current_affairs_quiz/
├── app.py              # Flask web app
├── db_setup.py         # SQLite DB setup
├── quiz_generator.py   # AI question generation logic
├── fetch_sources.py    # Fetch data from APIs + PDFs
├── templates/
│   ├── quiz.html       # Quiz page
│   └── results.html    # Results page
└── pdfs/               # Store monthly/yearly PDFs here


---

## ⚙️ Setup Instructions

### 1. Clone & Enter Project
```bash
cd ~/sambasrc/agent

2. Create Virtual Environment

python3 -m venv agent_venv
source agent_venv/bin/activate   # Linux/Mac
agent_venv\Scripts\activate      # Windows

3. Install Dependencies

pip install -r requirements.txt

Usage
Step 1: Initialize Database
python3 db_setup.py

Step 2: Fetch Sources
Add PDFs to the pdfs/ folder.

Run:
python3 fetch_sources.py

This will pull facts from NewsAPI, RSS feeds, and PDFs, then store questions in SQLite.

Step 3: Run Flask App
python3 app.py

Open in browser:

Inside VM: http://127.0.0.1:5000

From Windows host: http://<VM_IP>:5000 (ensure port forwarding or bridged networking in VirtualBox).

Features
Data ingestion: NewsAPI, RSS feeds, PDFs.

AI question generation: Hugging Face T5 + DistilBERT QA.

Dynamic options: Distractors generated automatically.

User interaction: Submit answers via web form.

Results tracking: See correct vs wrong answers.

Retry mode: Practice only wrong answers.

Requirements
See requirements.txt:

flask

requests

feedparser

pdfplumber

transformers

torch

Future Improvements
Add user accounts for personalized score tracking.

Expand distractor generation beyond countries (e.g., dates, organizations).

Schedule daily auto‑fetch with cron jobs.

---

✅ With this README, your project is now fully documented and portable.  

Would you like me to also add a **section in README about VirtualBox networking setup** (NAT port forwarding vs Bridged Adapter) so you can always access Flask from Windows Chrome without confusion?

Notes
If you don’t want AI models yet, you can remove transformers and torch from the file.

If you later add more NLP libraries (like spacy or nltk), just append them here.

Keeping everything in requirements.txt makes your project portable — anyone can set it up with a single command.

🚀 Current Capabilities
Data ingestion: APIs + RSS + PDFs.

AI generation: Hugging Face models for natural questions + answers.

Dynamic options: Distractors generated automatically.

User interaction: Submit answers, see results, retry wrong ones.

Learning loop: System adapts to user mistakes for reinforcement.

-----------------------------
File Based description
-----------------------------

6. templates/results.html
New file added:

Shows each question, user’s selected answer, correct answer, and correctness status.

Provides link to /retry for practicing wrong answers.

5. templates/quiz.html
Initial: Displayed questions and options statically.

Improved:

Added <form> with radio buttons for each option.

Submits answers to Flask backend.

Keeps question IDs in form names (q_<id>) for DB linkage.

4. app.py
Initial: Simple Flask app serving random questions from DB.

Improved:

Added form submission to capture user answers.

Inserted responses into responses table with correctness flag.

Added /results route to show user answers vs correct answers.

Added /retry route to regenerate quiz only from wrong answers.

Changed app.run(host="0.0.0.0") so it’s accessible from Windows browser via VM IP.


3. fetch_sources.py
Initial: Pulled facts from NewsAPI, RSS feeds, and PDFs.

Improved:

Added import os to handle folder scanning.

fetch_all_pdfs() loops through pdfs/ folder and processes all PDFs automatically.

Unified pipeline: NewsAPI + RSS + PDFs → save_question().

2. quiz_generator.py
Initial: Simple template logic with static options (India, USA, China, Japan).

Improved:

Integrated Hugging Face pipelines:

T5 for question generation.

DistilBERT QA for answer extraction.

Added dynamic distractor generation (random sampling from a pool of countries).

save_question() now stores AI‑generated question, options, and correct answer in DB.

1. db_setup.py
Initial: Only had a questions table to store facts, questions, options, and answers.

Improved: Added a responses table to log user answers, correctness, and link back to the question.

CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    selected_answer TEXT,
    correct INTEGER,
    FOREIGN KEY(question_id) REFERENCES questions(id)
);

