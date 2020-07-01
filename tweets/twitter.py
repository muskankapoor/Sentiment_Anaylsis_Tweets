import tweepy

from . import Tweeter
import error

class Twitter(Tweeter):
    def __init__(self, cons_key, cons_secret):
        auth = tweepy.AppAuthHandler(cons_key, cons_secret)
        self._api = tweepy.API(auth)

    def get_tweet_text(self, tweet_id):
        try:
            status = self._api.get_status(tweet_id)
            return status.text
        except tweepy.error.TweepError as e:
            if e.api_code == 144:
                raise error.TweetNotFoundError
