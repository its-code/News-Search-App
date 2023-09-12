# Importing Necessary Modules
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


# NEWS API and URL CONSTANTS:
NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""


# Router for NEWS Search
@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    language = request.json.get('language', 'en')
    one_month_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    response = requests.get(NEWS_API_URL, params={
        'q': query,
        'language': language,
        'apiKey': NEWS_API_KEY,
        'from': one_month_ago
    })
    
    news_data = response.json()
    articles = news_data.get('articles', [])
    
    # Sending the Results
    results = [
        {
            'title': article['title'],
            'url': article['url'],
            'thumbnail': article.get('urlToImage')
        }
        for article in articles
    ]
    
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
