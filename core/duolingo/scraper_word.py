import asyncio
from playwright.async_api import Page
from utils.data.tags import *
from core.duolingo.db_writer import db_writer


async def scraper(page: Page) -> None:
    """Данный модуль парсит слова уже с тренировочного хаба"""
    # known_words_dictionary = await takeold_words()
    print("Parsing Mode active...")
    print("Waiting for initialise button for loading more/new words...")
    await asyncio.sleep(5)
    more_words_click = page.locator(
        DOWNLOAD_MORE_BUTTON, has_text=DOWNLOAD_MORE_BUTTON_INNER_TEXT
    )
    while await more_words_click.count() > 0:
        print("Detected button loader...")
        await more_words_click.scroll_into_view_if_needed()
        await more_words_click.click(force=True)
        print("Button has been clicked...")
        await asyncio.sleep(5)
    await asyncio.sleep(5)
    print("All iterations succesfully complete...")
    default_words = await page.locator(DEFAULT_WORDS_TAG).all_inner_texts()
    translate_words = await page.locator(TRANSLATED_WORDS_TAG).all_inner_texts()
    print(
        f"стандартный список слов {default_words}, список переведенных слов {translate_words}"
    )
    await db_writer(default_words, translate_words)