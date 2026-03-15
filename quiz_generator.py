import sqlite3
import random
from transformers import pipeline

# Load Hugging Face pipelines
qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-small-qa-qg-hl")
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# A pool of distractors (you can expand this list)
COUNTRIES = ["India", "USA", "China", "Japan", "Pakistan", "South Korea", "UK", "Germany"]

def generate_ai_question(fact):
    # Step 1: Generate a question from the fact
    qg_result = qg_pipeline(f"generate question: {fact}", max_length=64, do_sample=False)
    question = qg_result[0]['generated_text']

    # Step 2: Extract the correct answer from the fact
    qa_result = qa_pipeline(question=question, context=fact)
    answer = qa_result['answer']

    # Step 3: Generate dynamic options
    distractors = random.sample([c for c in COUNTRIES if c != answer], 3)
    options = [answer] + distractors
    random.shuffle(options)

    return question, options, answer

def save_question(fact):
    question, options, answer = generate_ai_question(fact)
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("INSERT INTO questions (fact, question, option_a, option_b, option_c, option_d, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (fact, question, options[0], options[1], options[2], options[3], answer))
    conn.commit()
    conn.close()
