from abc import ABC, abstractmethod

from essential_generators import DocumentGenerator

class Tweeter(ABC):
    @abstractmethod
    def get_tweet_text(self, tweet_id):
        pass

class RandomTweeter(Tweeter):
    def __init__(self):
        self._gen = DocumentGenerator()

    def get_tweet_text(self, tweet_id):
        return self._gen.sentence()

