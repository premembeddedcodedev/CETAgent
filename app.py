from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_questions():
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("SELECT id, question, option_a, option_b, option_c, option_d, answer FROM questions ORDER BY RANDOM() LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        # Save user answers
        for key, value in request.form.items():
            qid = int(key.split("_")[1])  # question_id from form name
            selected = value
            conn = sqlite3.connect("quiz.db")
            c = conn.cursor()
            # Check correctness
            c.execute("SELECT answer FROM questions WHERE id=?", (qid,))
            correct_answer = c.fetchone()[0]
            correct = 1 if selected == correct_answer else 0
            c.execute("INSERT INTO responses (question_id, selected_answer, correct) VALUES (?, ?, ?)",
                      (qid, selected, correct))
            conn.commit()
            conn.close()
        return redirect(url_for("results"))

    questions = get_questions()
    return render_template("quiz.html", questions=questions)

@app.route("/results")
def results():
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("SELECT q.question, r.selected_answer, q.answer, r.correct FROM responses r JOIN questions q ON r.question_id=q.id ORDER BY r.id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return render_template("results.html", results=rows)

@app.route("/retry")
def retry_wrong():
    # Regenerate quiz only from wrong answers
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("SELECT q.id, q.question, q.option_a, q.option_b, q.option_c, q.option_d, q.answer FROM responses r JOIN questions q ON r.question_id=q.id WHERE r.correct=0 ORDER BY RANDOM() LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return render_template("quiz.html", questions=rows)

