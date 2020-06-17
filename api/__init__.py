from flask import Flask
from flask_cors import CORS

from sentiment import RandomSentimenter
from tweets import RandomTweeter

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/sentiment_analyses/<int:tweet_id>')
def tweet_analysis(tweet_id):
    # tweeter = RandomTweeter()
    sentimenter = RandomSentimenter()

    # text = tweeter.get_tweet_text(tweet_id)
    return sentimenter.analyze_text('')
