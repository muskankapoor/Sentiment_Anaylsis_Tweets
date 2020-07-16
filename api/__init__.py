import os

from flask import Flask, jsonify
from flask_cors import CORS

import error
from cache.sqlite import SqliteCache
from sentiment.caching import CachingSentimenter
from sentiment.watson import Watson
from tweets.twitter import Twitter

CACHE_DB_PATH = 'db/cache.db'

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

twitter = Twitter(os.environ.get('TWITTER_CONSUMER_KEY'),
                  os.environ.get('TWITTER_CONSUMER_SECRET'))

@app.route('/api/v1/sentiment_analyses/<int:tweet_id>')
def tweet_analysis(tweet_id):
    cache = SqliteCache("sentiments", CACHE_DB_PATH)
    watson = Watson()
    sentimenter = CachingSentimenter(cache, watson)

    try:
        text = twitter.get_tweet_text(tweet_id)
    except error.TweetNotFoundError:
        return jsonify(error='No tweet found with that ID.'), 404

    analysis_json = sentimenter.analyze_text(text)
    analysis_json['tweet_text'] = text
    return analysis_json
