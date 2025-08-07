import os
import json
async def takeold_words():
    try:
        if os.path.exists("words.json"):
            with open("words.json", "r", encoding="utf-8") as known_words_dictionary_container:
                known_words_set = json.load(known_words_dictionary_container)
                return known_words_set
        else:
            with open("words.json", "w", encoding="utf-8") as empty_file:
                empty_file.write("")
    except FileNotFoundError:
        pass