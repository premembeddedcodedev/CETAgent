import os
import requests, feedparser, pdfplumber, sqlite3
from quiz_generator import save_question

# --- NewsAPI ---
def fetch_newsapi():
    API_KEY = "b0707aea9e5e4d28834560e0e886a72f"
    url = f"https://newsapi.org/v2/everything?q=India&from=2025-03-01&to=2026-03-01&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    for article in articles[:10]:
        fact = article["title"]
        save_question(fact)

# --- Google News RSS ---
def fetch_rss():
    feed = feedparser.parse("https://news.google.com/rss/search?q=India+current+affairs")
    for entry in feed.entries[:10]:
        fact = entry.title
        save_question(fact)

# --- PDF Parsing (Vision IAS, Arihant, etc.) ---
#def fetch_pdf(path):
#    with pdfplumber.open(path) as pdf:
#        for page in pdf.pages:
#            text = page.extract_text()
#            if not text: continue
#            for line in text.split("\n"):
#                if line.strip():
#                    save_question(line)

def fetch_all_pdfs(folder="pdfs"):
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if not text: continue
                    for line in text.split("\n"):
                        if line.strip():
                            save_question(line)

if __name__ == "__main__":
    # fetch_newsapi()
    # fetch_rss()
    # Example: parse one monthly PDF
    # fetch_pdf("VisionIAS_Feb2026.pdf")
    fetch_all_pdfs()    

