import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from sentiment import Sentimenter

#authenticator = IAMAuthenticator('{apikey}')
#tone_analyzer = ToneAnalyzerV3(
#    version='{version}',
#    authenticator=authenticator
#)
# tone_analyzer.set_service_url('{url}')

# Authentication via external config like VCAP_SERVICES
tone_analyzer = ToneAnalyzerV3(version='2020-06-17')
tone_analyzer.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

# text = "this is a sample tweet #analyze" 
# print(json.dumps(tone_analysis, indent=2))

class WatsonSentimenter(Sentimenter):            
    def analyze_text(self, text):
        tone_analysis = tone_analyzer.tone({'text': text}, content_type='application/json' ).get_result()
        return tone_analysis

#   def generate_random_analysis(self):
#       return {
#           'document_tone': {
#               'tones': self.generate_random_tones(random.randint(1, 7)),
#           },
#       }
#
#   def generate_random_tones(self, n):
#       '''
#       Generate n random tone scores, without repeating tones.
#       '''
#
#       tone_ids = ['anger', 'fear', 'joy', 'sadness',
#                   'analytical', 'confident', 'tentative']
#       n = min(n, len(tone_ids))
#       random.shuffle(tone_ids)
#
#       tones = []
#       for i in range(n):
#           tone = {
#               'score': random.random(),
#               'tone_id': tone_ids.pop(),
#           }
#           tones.append(tone)
#
#       return tones
#
#
