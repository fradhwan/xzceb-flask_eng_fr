import unittest
from translator import french_to_english, english_to_french

class Translations(unittest.TestCase):

    def test_englishToFrench(self):
        enToFr = english_to_french("Hello")
        self.assertEqual(enToFr,"Bonjour", "The tr is not accurate.")

    def test_frenchToEnglish(self):
        frToEn = french_to_english("Bonjour")
        self.assertEqual(frToEn,"Hello", "The tr is not accurate.")

if __name__ == '__main__':
    unittest.main()