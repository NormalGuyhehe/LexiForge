import os
from utils.data.get_words import get_dictionary_from_file
from core.generator.LLM_module.ai_note_generator import note_generator
from utils.tools.get_playwright_object import take_playwright_object
from playwright.async_api import Page
async def notes_writer(current_dir, vault_path):
    words_dict_or_set: dict = await get_dictionary_from_file(current_dir)
    os.chdir(vault_path)
    print(os.listdir(vault_path))
    openAI_page: Page = take_playwright_object() 
    for default_word, translate in words_dict_or_set.items():
        print(default_word, translate)
        # note_text = await note_generator()