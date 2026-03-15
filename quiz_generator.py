import sqlite3

def generate_question_from_fact(fact):
    question = f"Which event is related to: {fact}?"
    options = ["India", "USA", "China", "Japan"]
    answer = "India" if "India" in fact else options[1]
    return question, options, answer

def save_question(fact):
    question, options, answer = generate_question_from_fact(fact)
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("INSERT INTO questions (fact, question, option_a, option_b, option_c, option_d, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (fact, question, options[0], options[1], options[2], options[3], answer))
    conn.commit()
    conn.close()

