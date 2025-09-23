from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncGenerator
from playwright.async_api import async_playwright, Page


@lru_cache
@asynccontextmanager
# used special context manager from standart python lib for correct create and live cycle object of Page class
async def take_for_duolingo_playwright_object() -> AsyncGenerator[Page]:
    print("Getting playwright object...")
    """This function take the object of playwright class Page from sync_api"""

    async with async_playwright() as pw:
        print("configuring of setting object...")
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.clear_cookies()
        print("create Page object...")
        page = await context.new_page()
        try:
            print("takes page object...")
            yield page
        finally:
            await browser.close()
