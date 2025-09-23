"""get user words"""

from utils.tools.duolingo_playwright_object import take_for_duolingo_playwright_object
from core.duolingo.login_duolingo import login_and_scraping_duolingo
from functools import lru_cache


@lru_cache
async def get_data():
    print("Launch duolingo core...")
    """This module get object of class Playwright from playwright lib,
        and get user data from function take_user_data_duolingo,
        after all, he is auth on duolingo user account and scraping only
        ----------------------------------------------------------------
        LEARNED WORDS, NO MORE, NO LESS
        ----------------------------------------------------------------
        """
    async with take_for_duolingo_playwright_object() as page:
        print(
            "Page object succefully initialised, start authorise of duolingo account..."
        )
        await login_and_scraping_duolingo(page)
