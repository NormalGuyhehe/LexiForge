"""Auth script"""
from playwright.sync_api import Page
def to_profile(page: Page, take_user_data_duolingo) -> None:
    """Auth into user profile"""
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