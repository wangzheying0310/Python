class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def letter_count(self):
        return len(self.sentence)

    def word_count(self):
        return len(self.sentence.split(" "))

    def upper(self):
        return self.sentence.upper()
