import requests
from bs4 import BeautifulSoup
from newspaper import Article

def scrape_article(url):
    # newspaper3k
    article = Article(url)
    try:
        article.download()
        article.parse()
        return article.text
    except:
        # if newspaper3k fails
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        article_text = ''
        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text()

        return article_text
