import random

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/sentiment_analyses/<int:tweet_id>')
def tweet_analysis(tweet_id):
    return generate_random_analysis()

def generate_random_analysis():
    return {
        'document_tone': {
            'tones': generate_random_tones(random.randint(1, 7)),
        },
    }

def generate_random_tones(n):
    '''
    Generate n random tone scores, without repeating tones.
    '''

    tone_ids = ['anger', 'fear', 'joy', 'sadness', 'analytical', 'confident', 'tentative']
    n = min(n, len(tone_ids))
    random.shuffle(tone_ids)

    tones = []
    for i in range(n):
        tone = {
            'score': random.random(),
            'tone_id': tone_ids.pop(),
        }
        tones.append(tone)

    return tones
