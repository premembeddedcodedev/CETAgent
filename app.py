from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_questions():
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("SELECT question, option_a, option_b, option_c, option_d, answer FROM questions ORDER BY RANDOM() LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows

@app.route("/")
def quiz():
    questions = get_questions()
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
#    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
