from utils.data.tags import *
from playwright.async_api import Page


async def logout(page: Page):
    print("Find options button...")
    options: object = page.locator(
        MORE_OPTIONS_TAG, has_text=MORE_OPTIONS_TAG_INNER_TEXT
    )
    await options.click()
    print("Focus on button for unblocked new button...")
    get_out_button: object = page.locator(LOG_OUT_BUTTON_TAG)
    await get_out_button.click()
    print("Get out button has clicked, process works complete ✔")
