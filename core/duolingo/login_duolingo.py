"""Login Duolingo and scraping data"""
import time
from playwright.sync_api import Page
from utils.user.get_user_data_duolingo import take_user_data_duolingo
def login_and_scraping_duolingo(page:Page):
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
                train_button = page.locator('[data-test="practice-hub-nav"]')
                train_button.click(force=True)
                action_to_words = page.locator('[data-test="practice-hub-collection-button"]', has_text="Повторяйте слова из курса английского в любое время")
                action_to_words.scroll_into_view_if_needed()
                action_to_words.click()
                if page.locator('[data-test="plus-no-thanks"]').count() > 0:
                    button = page.locator('[data-test="plus-no-thanks"]')
                    button.first.click(force=True)
                more_words_click = page.locator('li[role="button"]', has_text="Загрузить больше")
                while True:
                    if more_words_click.count() == 0:
                        words_list = page.locator("li").inner_text()
                        print(words_list)
                        break
                    else:
                        more_words_click.scroll_into_view_if_needed()
                        more_words_click.click(force=True)
            finally:
                get_out = page.locator('[data-test="more-nav"]')
                get_out.hover('[data-test="more-nav"]', force=True)
                log_out = page.locator('[data-test="logout-button"]')
                log_out.click(force=True)