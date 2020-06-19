from flask import Flask
from flask_cors import CORS

from cache.sqlite import SqliteCache
<<<<<<< HEAD
from sentiment.analyze import WatsonSentimenter
||||||| merged common ancestors
from sentiment import RandomSentimenter
=======
from sentiment import WatsonSentimenter
>>>>>>> 69923d57a0d4a5030d2534aa7a541cbc05b26970
from sentiment.caching import CachingSentimenter

CACHE_DB_PATH = 'db/cache.db'

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/sentiment_analyses/<int:tweet_id>')
def tweet_analysis(tweet_id):
    cache = SqliteCache("sentiments", CACHE_DB_PATH)
    watson_sent = WatsonSentimenter()
    sentimenter = CachingSentimenter(cache, random_sent)

    return sentimenter.analyze_text(str(tweet_id))
