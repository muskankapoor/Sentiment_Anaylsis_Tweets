import os
import unittest

<<<<<<< HEAD
from sentiment import WatsonSentimenter
||||||| merged common ancestors
from sentiment.analyze import WatsonSentimenter
#
#class WatsonSentimenterTest(unittest.TestCase):
#    def test_watsonsentimenter(self):
#        self.assertEqual(self.WatsonSentimenter.analyze_text('hello'),' ')
#
=======
from sentiment import WatsonSentimenter
#
#class WatsonSentimenterTest(unittest.TestCase):
#    def test_watsonsentimenter(self):
#        self.assertEqual(self.WatsonSentimenter.analyze_text('hello'),' ')
#
>>>>>>> 69923d57a0d4a5030d2534aa7a541cbc05b26970
#
class WatsonSentimenterTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_watsonsentimenter(self):
        self.assertEqual(self.WatsonSentimenter.analyze_text('hello'),' ')


        
