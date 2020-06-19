import os
import unittest

from sentiment.analyze import WatsonSentimenter

class WatsonSentimenterTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_watsonsentimenter(self):
        self.assertEqual(self.WatsonSentimenter.analyze_text(
            """I hate these new features On #ThisPhone after the update. I hate #ThisPhoneCompany products, you'd have to torture me to get me to use #ThisPhone. The emojis in #ThisPhone are stupid. #ThisPhone is a useless, stupid waste of money. #ThisPhone is the worst phone I've ever had - ever. #ThisPhone another ripoff, lost all respect SHAME. I'm worried my #ThisPhone is going to overheat like my brother's did. #ThisPhoneCompany really let me down... my new phone won't even turn on."""
        ),
    {
  "document_tone": {
    "tones": [
      {
        "score": 0.565706,
        "tone_id": "fear",
        "tone_name": "Fear"
      },
      {
        "score": 0.647322,
        "tone_id": "anger",
        "tone_name": "Anger"
      },
      {
        "score": 0.724923,
        "tone_id": "confident",
        "tone_name": "Confident"
      }
    ]
  }
})


        
