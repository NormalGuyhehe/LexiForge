from typing import AsyncGenerator
from contextlib import asynccontextmanager
from playwright.async_api import async_playwright, Page
from functools import lru_cache


@lru_cache
@asynccontextmanager
# used special context manager from standart python lib for correct create and live cycle object of Page class
async def take_for_duolingo_playwright_object() -> AsyncGenerator[Page]:
    print("Getting playwright object...")
    """This function take the object of playwright class Page from sync_api"""
    async with async_playwright() as pw:
        print("configuring of setting object...")
        browser = await pw.firefox.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )
        await context.clear_cookies()
        print("create Page object...")
        page = await context.new_page()
        try:
            print("takes page object...")
            yield page
        finally:
            await browser.close()


@lru_cache
@asynccontextmanager
async def take_for_AI_playwright_object() -> AsyncGenerator[Page]:
    print("Getting playwright object...")
    """This function take the object of playwright class Page from sync_api"""
    async with async_playwright() as pw:
        print("configuring of setting object...")
        browser = await pw.chromium.launch_persistent_context(
            executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            headless=False,
            user_data_dir="C:/Users/Черный пацан/AppData/Local/Microsoft/Edge/User Data/Default",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )
        page = browser.pages[0] if browser.pages else await browser.new_page()
        try:
            print("takes page object...")
            yield page
        finally:
            await browser.close()
