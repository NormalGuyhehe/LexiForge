async def get_dictionary_from_file():
    with open("words.md", 'r', encoding="utf-8") as source:
        words = source.read()
        print(words)
        return words