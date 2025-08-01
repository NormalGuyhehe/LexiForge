"""Auth script"""
from utils.data.tags import *
from playwright.sync_api import Page
async def to_profile(page: Page, take_user_data_duolingo) -> None:
    """Auth into user profile"""
    info = await take_user_data_duolingo()
    
    await page.goto(DUOLINGO_URL)
    have_account = page.locator(HAVE_ACCOUNT_TAG)
    await have_account.click(force=True)

    if await page.locator(USE_ANOTHER_ACCOUNT_TAG).count() > 0:
        password_input = page.locator(PASSWORD_INPUT_TAG)
        await password_input.click(force=True)
        await password_input.fill(info[1])
        auth_button = page.locator(AUTH_BUTTON_TAG)
        await auth_button.click()
    else:
        email_input = page.locator(EMAIL_INPUT_TAG)
        password_input = page.locator(PASSWORD_INPUT_TAG)
        await email_input.click(force=True)
        await email_input.fill(info[0])
        await password_input.clear(force=True)
        await password_input.fill(info[1])
        auth_button = page.locator(AUTH_BUTTON_TAG)
        await auth_button.click()