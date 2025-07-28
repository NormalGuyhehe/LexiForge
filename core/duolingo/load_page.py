from utils.user.get_user_data_duolingo import take_user_data_duolingo
import time
from playwright.sync_api import sync_playwright
def get_page():
      with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.duolingo.com/")
            page.wait_for_selector('[data-test="have-account"]', timeout=5000)
            page.click('[data-test="have-account"]', force=True)
            page.wait_for_selector('[data-test="email-input"]', timeout=5000)
            page.wait_for_selector('[data-test="password-input"]', timeout=5000)
            info = take_user_data_duolingo()
            page.click('[data-test="email-input"]', force=True)
            page.fill('[data-test="email-input"]', info[0])
            page.click('[data-test="password-input"]', force=True)
            page.fill('[data-test="password-input"]', info[1])