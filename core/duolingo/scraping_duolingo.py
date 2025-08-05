from functools import lru_cache
from utils.data.tags import *
from playwright.async_api import Page
from core.duolingo.go_to_profile import to_profile
from core.duolingo.practice_hub import practice_hub
from core.duolingo.scraper_word import writer
from core.duolingo.logout import logout

@lru_cache
async def scrape_data(page: Page, take_user_data_duolingo):
    """Scrape and serialisation data"""
    try:
        await practice_hub(page)
        if await page.locator(NO_THANKS_TAG).count() > 0:
            print("Activate fallbacks...")
            button: object = page.locator(NO_THANKS_TAG)
            await button.first.click(force=True)
            print("Problem has been destroyed...")
        await writer(page) 
    except Exception as e:
        print(f"Finds error {e}, reload script...")
        await to_profile(page, take_user_data_duolingo)
    finally:
        await logout(page)