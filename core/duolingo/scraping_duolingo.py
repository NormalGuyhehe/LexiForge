from utils.data.tags import *
from playwright.async_api import Page
from core.duolingo.go_to_profile import to_profile
from core.duolingo.practice_hub import practice_hub
from core.duolingo.scraper_word import scraper
async def scrape_data(page: Page, take_user_data_duolingo):
    """Scrape and serialisation data"""
    try:
        await practice_hub(page)
        if await page.locator(NO_THANKS_TAG).count() > 0:
            print("Activate fallbacks")
            button: object = page.locator(NO_THANKS_TAG)
            await button.first.click(force=True)
            print("Problem has been destroyed...")
        await scraper(page) 
    except Exception as e:
        print(f"произошла ошибка {e}, перезапуск скрипта")
        await to_profile(page, take_user_data_duolingo)
    finally:
        print("Find options button...")
        options: object = page.locator(MORE_OPTIONS_TAG, has_text=MORE_OPTIONS_TAG_INNER_TEXT)
        await options.click()
        print("Focus on button for unblocked new button...")
        get_out_button: object = page.locator(LOG_OUT_BUTTON_TAG)
        await get_out_button.click()
        print("Get out button has clicked, process works complete ✔")