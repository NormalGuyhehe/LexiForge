"""Login Duolingo and scraping data"""
import time
from utils.user.get_user_data_duolingo import take_user_data_duolingo
def login_and_scraping_duolingo(page):
            """this module used next function :
            take_user_data_duolingo, he give in this function user 
            email and password for duolingo scraping"""
            page.goto("https://www.duolingo.com/")
            page.wait_for_selector('[data-test="have-account"]', timeout=5000)
            page.click('[data-test="have-account"]', force=True)
            page.wait_for_selector('[data-test="email-input"]', timeout=5000)
            page.wait_for_selector('[data-test="password-input"]', timeout=5000)
            info = take_user_data_duolingo()
            try:
                page.click('[data-test="email-input"]', force=True)
                page.fill('[data-test="email-input"]', info[0])
                page.click('[data-test="password-input"]', force=True)
                page.fill('[data-test="password-input"]', info[1])
            finally: 
                page.click('[data-test="password-input"]', force=True)
                page.fill('[data-test="password-input"]', info[1])
            page.click('[data-test="register-button"]', force=True)
            """
            ------------------------------------------------------------------------------ 
            """
            try:
                time.sleep(5)
                page.wait_for_selector('[data-test="practice-hub-nav"]', timeout=5000)
                page.hover('[data-test="practice-hub-nav"]', force=True)
                time.sleep(5)
                page.click('[data-test="practice-hub-nav"]', force=True)
                time.sleep(5)
                page.wait_for_selector('[data-test="practice-hub-collection-button"]', timeout=5000)
                time.sleep(5)
                page.click('[data-test="practice-hub-collection-button"]', force=True)
                time.sleep(5)
                while True:
                    page.wait_for_selector('[data-test="plus-no-thanks"]', timeout=5000)
                    page.click('[data-test="plus-no-thanks"]', force=True)
                    page.wait_for_selector('[role="button"]', timeout=5000)
                    page.click('[role="button"]', force=True)
            finally:
                pass
                # page.wait_for_selector('[data-test="more-nav"]', timeout=5000)
                # page.hover('[data-test="more-nav"]', force=True)
                # log_out = page.locator('[data-test="logout-button"]')
                # log_out.click(force=True)