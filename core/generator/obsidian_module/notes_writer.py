import os
from utils.data.get_words import get_dictionary_from_file
from core.generator.LLM_module.ai_note_generator import note_generator
from core.generator.LLM_module.ai_cards_generator import cards_generator
from utils.tools.get_playwright_object import take_for_AI_playwright_object
from playwright.async_api import Page


async def words_notes_writer(current_dir, vault_path):
    words_dict_or_set: dict = await get_dictionary_from_file(current_dir)
    print("notes module works...")
    os.chdir(vault_path)
    print(os.listdir())
    os.chdir("vocabulary")

    async with take_for_AI_playwright_object() as openAI_page:
        for default_word, translate in words_dict_or_set.items():
            vocabulary_note_text = await note_generator(openAI_page, default_word, translate)