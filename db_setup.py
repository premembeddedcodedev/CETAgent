import sqlite3

def init_db():
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  fact TEXT,
                  question TEXT,
                  option_a TEXT,
                  option_b TEXT,
                  option_c TEXT,
                  option_d TEXT,
                  answer TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

