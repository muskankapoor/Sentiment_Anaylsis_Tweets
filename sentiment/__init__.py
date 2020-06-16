from abc import ABC, abstractmethod
import random

class Sentimenter(ABC):
    @abstractmethod
    def analyze_text(self, text):
        pass

class RandomSentimenter(Sentimenter):
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def analyze_text(self, text):
        return self.generate_random_analysis()


    def generate_random_analysis(self):
        return {
            'document_tone': {
                'tones': self.generate_random_tones(random.randint(1, 7)),
            },
        }

    def generate_random_tones(self, n):
        '''
        Generate n random tone scores, without repeating tones.
        '''

        tone_ids = ['anger', 'fear', 'joy', 'sadness',
                    'analytical', 'confident', 'tentative']
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
