class TextAnalyzer:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, filename: str) -> None:
        self.file = open(filename, 'r')
        self.words: list = []
        self.words_counter: dict = {}

    def load_text(self) -> None:
        for row in self.file:
            words_in_row = row.split()
            for word in words_in_row:
                if word[-1] not in self.ALPHABET and word[-1] not in self.ALPHABET.upper():
                    self.words.append(word[:-1].lower())
                else:
                    self.words.append(word.lower())

    def count_words(self):
        for word in self.words:
            if word in self.words_counter.keys():
                self.words_counter[word] += 1
            else:
                self.words_counter[word] = 1

    def get_top_words(self) -> list:
        top_words: list = []
        max_counter: int = max([i for i in self.words_counter.values()])
        for key, value in self.words_counter.items():
            if value == max_counter:
                top_words.append(key)
        return top_words

    def get_bottom_words(self) -> list:
        top_words: list = []
        min_counter: int = min([i for i in self.words_counter.values()])
        for key, value in self.words_counter.items():
            if value == min_counter:
                top_words.append(key)
        return top_words
