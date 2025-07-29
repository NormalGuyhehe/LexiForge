from playwright.sync_api import sync_playwright
from contextlib import contextmanager

@contextmanager
def take_playwright_object() -> object:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            yield page
        finally:
            browser.close()