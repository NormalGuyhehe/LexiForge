import json
async def db_writer(default_word_list: list, translate_word_list: list):
    translate_word_list.pop(0)
    print("Getting all words and zip to smart dictionary...")
    vocab_dictionary = dict(zip(default_word_list, translate_word_list))
    with open("words.json", "w", encoding="utf-8") as word_container:
        json.dump(vocab_dictionary, word_container, ensure_ascii=False, indent=4)
        word_container.close()