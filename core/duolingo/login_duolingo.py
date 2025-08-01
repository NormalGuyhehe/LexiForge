"""Login Duolingo and scraping data"""
import time
from playwright.sync_api import Page
from utils.user.get_user_data_duolingo import take_user_data_duolingo
from core.duolingo.go_to_profile import to_profile
from core.duolingo.scraping_duolingo import scrape_data
async def login_and_scraping_duolingo(page:Page):
            """this module used next function :
            take_user_data_duolingo, he give in this function user 
            email and password for duolingo scraping"""
            print("launch auth module...")
            await to_profile(page, take_user_data_duolingo)
            print("Succesfully complete...")
            print("Start of scraping data...")
            await scrape_data(page, take_user_data_duolingo)
                # get_out = page.locator('[data-test="more-nav"]')
                # get_out.hover('[data-test="more-nav"]', force=True)
                # log_out = page.locator('[data-test="logout-button"]')
                # log_out.click(force=True)