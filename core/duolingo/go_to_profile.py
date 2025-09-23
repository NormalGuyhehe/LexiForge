"""Auth script"""

from functools import lru_cache
import asyncio
import random

from playwright.sync_api import Page

from utils.data.tags import *


@lru_cache
async def to_profile(page: Page, take_user_data_duolingo) -> None:
    """Auth into user profile"""
    info = await take_user_data_duolingo()
    print("go to duolingo...")
    await page.goto(DUOLINGO_URL, wait_until="domcontentloaded")
    await page.evaluate("localStorage.clear()")
    await page.evaluate("sessionStorage.clear()")
    have_account = page.locator(HAVE_ACCOUNT_TAG)
    await have_account.click(force=True)
    print("auth process...")
    email_input = page.locator(EMAIL_INPUT_TAG)
    password_input = page.locator(PASSWORD_INPUT_TAG)
    await email_input.click(force=True)
    await email_input.fill(info[0])
    await password_input.clear(force=True)
    await password_input.fill(info[1])
    auth_button = page.locator(AUTH_BUTTON_TAG)
    print("user data injected...")
    await auth_button.click()
    await asyncio.sleep(random.uniform(0.5, 1.5))
    while (
        await page.locator(
            USE_ANOTHER_ACCOUNT_TAG, has_text=USE_ANOTHER_ACCOUNT_TEXT_RUS
        ).count()
        > 0
    ):
        use_another_account_tag_button_object = page.locator(
            USE_ANOTHER_ACCOUNT_TAG, has_text=USE_ANOTHER_ACCOUNT_TEXT_RUS
        )
        await use_another_account_tag_button_object.click(force=True)
        email_input = page.locator(EMAIL_INPUT_TAG)
        await email_input.click(force=True)
        await email_input.fill(info[0])
        password_input = page.locator(PASSWORD_INPUT_TAG)
        await password_input.click(force=True)
        await password_input.fill(info[1])
        await auth_button.click()
        await asyncio.sleep(random.uniform(0.5, 1.5))

    while (
        await page.locator(
            USE_ANOTHER_ACCOUNT_TAG, has_text=USE_ANOTHER_ACCOUNT_TEXT_ENG
        ).count()
        > 0
    ):
        use_another_account_tag_button_object = page.locator(
            USE_ANOTHER_ACCOUNT_TAG, has_text=USE_ANOTHER_ACCOUNT_TEXT_ENG
        )
        use_another_account_tag_button_object.click(force=True)
        email_input = page.locator(EMAIL_INPUT_TAG)
        await email_input.click(force=True)
        await email_input.fill(info[0])
        password_input = page.locator(PASSWORD_INPUT_TAG)
        await password_input.click(force=True)
        await password_input.fill(info[1])
        await auth_button.click()
        await asyncio.sleep(random.uniform(0.5, 1.5))