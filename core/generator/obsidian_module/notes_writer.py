import os
from utils.data.get_words import get_dictionary_from_file
async def notes_writer(vault_path):
    os.chdir(vault_path)
    print(os.listdir())
    words_dict_or_set = await get_dictionary_from_file()
    print(type(words_dict_or_set))
