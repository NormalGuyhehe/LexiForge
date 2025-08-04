import asyncio
from utils.data.tags import *
from playwright.async_api import Page

async def writer(page: Page):
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
            with open("words.md", "a+", encoding="utf-8") as word_container:
                word_container.write(f"{vocab_dictionary}\n")
                word_container.close()
            break