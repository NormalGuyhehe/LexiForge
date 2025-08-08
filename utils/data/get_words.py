import os
async def get_dictionary_from_file():
    print(os.listdir())
    with open("words.json", "r", encoding="utf-8") as source:
        words = source.read()
        print(words)
        return words