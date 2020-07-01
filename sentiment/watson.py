import json

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from sentiment import Sentimenter

# Authentication via external config like VCAP_SERVICES
tone_analyzer = ToneAnalyzerV3(version='2020-06-17')

class Watson(Sentimenter):
    def analyze_text(self, text):
        analysis = tone_analyzer.tone(
            {'text': text},
            content_type='application/json'
        ).get_result()
        return analysis
