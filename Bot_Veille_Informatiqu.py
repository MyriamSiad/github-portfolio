
import feedparser
from flask import Flask, render_template
from bs4 import BeautifulSoup

## Création d'un fichier XML Google Actualités sur Inoreader contenant le Flux de recherche Machine Learning
## url : 'https://news.google.com/news/rss/search?q=Machine%20learning&hl=fr-FR&gl=FR&ceid=FR:fr'

## Création d'une fonction qui recupère juste un nombre limités de Artciles, les plus récents

app = Flask(__name__)

def derniers_articles():
    feed = feedparser.parse('https://www.microsoft.com/en-us/research/feed/')
    articles = []

    for entry in feed.entries[:5]:
        title = entry.title
        link = entry.link

        summary_html = entry.summary
        summary_text = BeautifulSoup(summary_html, "html.parser").get_text()  # Extrait le texte sans HTML
        articles.append({"title": title, "summary": summary_text, "link": link})

    return articles

@app.route("/")
def index():
    articles = derniers_articles()
    return render_template("veille_informatique.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)



