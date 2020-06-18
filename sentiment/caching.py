import json

from . import Sentimenter

class CachingSentimenter(Sentimenter):
    def __init__(self, cache, next_sent):
        self._cache = cache
        self._next = next_sent

    def analyze_text(self, text):
        analysis_json = self._cache.get(text)
        if analysis_json:
            return json.loads(analysis_json)

        analysis = self._next.analyze_text(text)
        self._cache.put(text, json.dumps(analysis))
        return analysis
