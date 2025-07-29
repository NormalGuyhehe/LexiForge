"""get user words"""
from utils.user.get_user_data_duolingo import take_user_data_duolingo
from utils.tools.get_playwright_object import take_playwright_object
from core.duolingo.login_duolingo import login_and_scraping_duolingo
def get_data():
        """This module get object of class Playwright from playwright lib,
        and get user data from function take_user_data_duolingo,
        after all, he is auth on duolingo user account and scraping only
        ----------------------------------------------------------------
        LEARNED WORDS, NO MORE, NO LESS
        ----------------------------------------------------------------
        """
        with take_playwright_object() as page:
            login_and_scraping_duolingo(page=page)