import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour", "Not Equal")
        self.assertEqual(english_to_french("Hello, how are you?"), "Bonjour, comment es-tu?", "Not Equal")
        self.assertNotEqual(self, '', "English Text String is Empty")

class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello", "Not Equal")
        self.assertEqual(french_to_english("Bonjour, comment es-tu?"), "Hello, how are you?", "Not Equal")
        self.assertNotEqual(self, '', "French Text String is Null")

unittest.main()
