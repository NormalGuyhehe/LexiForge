# core/duolingo_api.py

from duolingo_api import Duolingo

class DuolingoClient:
    def __init__(self, username: str, password: str):
        self.client = Duolingo(username, password)

    def get_vocabulary(self, lang='en'):
        vocab = self.client.get_vocabulary(lang)
        result = []
        for word_data in vocab:
            word = word_data.get("word")
            if word:
                result.append(word.strip())
        return result
