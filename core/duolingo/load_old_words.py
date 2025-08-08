import os
import json
async def takeold_words():
    try:
        if os.path.exists("words.json"):
            with open("words.json", "r", encoding="utf-8") as known_words_dictionary_container:
                known_words_set = json.load(known_words_dictionary_container)
                return known_words_set
    except FileNotFoundError:
        # with open("") as 
        pass