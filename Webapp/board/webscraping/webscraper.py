import requests
from bs4 import BeautifulSoup
from newspaper import Article
import os
import requests

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



# hugging face

API_URL = "https://api-inference.huggingface.co/models/d4data/bias-detection-model"
headers = {"Authorization": os.environ.get('HUGGING_FACE')}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def inference(url):
    raw_text = scrape_article(url).split()
    scores = [0, 0]
    count = 0
    while len(raw_text) > 0:
        chunk = raw_text[:min(len(raw_text), 250)]
        output = query({
            "inputs": "".join(chunk),
        })
        scores[0] += output[0][0]['score']
        scores[1] += output[0][1]['score']
        raw_text = raw_text[len(chunk):]
        count+=1

    scores[0] = scores[0] / count 
    scores[1] = scores[1] / count 

    return scores

# print(inference(url))

