import unittest
from sentence import Sentence


class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence("HelloWorld!")

    def test_str_count(self):
        self.assertEqual(self.sentence.letter_count(), 12)

    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(), 2)

    def test_upper(self):
        self.assertEqual(self.sentence.upper(), "HELLOWORLD!")
