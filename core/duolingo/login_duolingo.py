"""Login Duolingo and scraping data"""
import time
from playwright.sync_api import Page
from utils.user.get_user_data_duolingo import take_user_data_duolingo
from core.duolingo.go_to_profile import to_profile
from core.duolingo.scraping_duolingo import scrape_data
def login_and_scraping_duolingo(page:Page):
            """this module used next function :
            take_user_data_duolingo, he give in this function user 
            email and password for duolingo scraping"""

            """
            ------------------------------------------------------------------------------ 
            """
            to_profile(page, take_user_data_duolingo)
            scrape_data(page)
                # get_out = page.locator('[data-test="more-nav"]')
                # get_out.hover('[data-test="more-nav"]', force=True)
                # log_out = page.locator('[data-test="logout-button"]')
                # log_out.click(force=True)