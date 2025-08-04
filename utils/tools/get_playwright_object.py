from typing import AsyncGenerator
from contextlib import asynccontextmanager
from playwright.async_api import async_playwright, Page

@asynccontextmanager
#used special context manager from standart python lib for correct create and live cycle object of Page class
async def take_playwright_object() -> AsyncGenerator[Page]:
    print("Getting playwright object...")
    """This function take the object of playwright class Page from sync_api"""
    async with async_playwright() as pw:
        print("configuring of setting object...")
        browser = await pw.chromium.launch(headless=False)
        print("create Page object...")
        page = await browser.new_page()
        try:
            print("takes page object...")
            yield page
        finally:
            await browser.close()