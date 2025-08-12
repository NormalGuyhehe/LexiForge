import os
from utils.data.get_words import get_dictionary_from_file
async def notes_writer(current_dir, vault_path):
    words_dict_or_set: dict = await get_dictionary_from_file(current_dir)
    os.chdir(vault_path)
    print(os.listdir(vault_path))
    for default_word in words_dict_or_set.keys():
        pass