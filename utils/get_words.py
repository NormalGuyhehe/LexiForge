import os
import json
async def get_dictionary_from_file():
    with open("words.json", "r", encoding="utf-8") as source:
        words_title = json.load(source)
        return words_title