import os
import json
import asyncio
from playwright.async_api import Page
from utils.data.tags import *
from core.duolingo.load_old_words import takeold_words

async def writer(page: Page):
    known_words_dictionary = await takeold_words()
    while True:
        print("Parsing Mode active...")
        print("Waiting for initialise button for loading more/new words...")
        await asyncio.sleep(3)
        more_words_click = page.locator(DOWNLOAD_MORE_BUTTON, has_text=DOWNLOAD_MORE_BUTTON_INNER_TEXT)
        print("Detected button loader...")
        if await more_words_click.count() > 0:
            await more_words_click.scroll_into_view_if_needed()
            await more_words_click.click(force=True)
            print("Button has been clicked...")
        elif await more_words_click.count() == 0:
            print("All iterations succesfully complete...")
            default_words = await page.locator(DEFAULT_WORDS_TAG).all_inner_texts()
            translate_words = await page.locator(TRANSLATED_WORDS_TAG).all_inner_texts()
            print("Getting all words and zip to smart dictionary...") 
            vocab_dictionary = dict(zip(default_words, translate_words))
            with open("words.json", "a+", encoding="utf-8") as word_container:
                for word, translation in vocab_dictionary.items():
                    if word not in known_words_dictionary:
                        print(f"WRITE {word} - {translation}")
                        known_words_dictionary[word] = translation
                        print(known_words_dictionary)
                        word_container.write(f"{word} - {translation}\n")
                    else:
                        print(f"[PASS] - {word}, {translation}")
                        continue
            break