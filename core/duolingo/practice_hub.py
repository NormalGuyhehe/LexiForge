import asyncio
import random
from functools import lru_cache
from utils.data.tags import *
from playwright.async_api import Page


@lru_cache
async def practice_hub(page: Page) -> None:
    await asyncio.sleep(random.uniform(1.5, 3.0))
    print("Login into practice hub...")
    train_button = page.locator(PRACTICE_HUB_TAG)
    print("Element has been finded...")
    await train_button.click(force=True)
    print("Button clicked succesfully...")
    await asyncio.sleep(random.uniform(1.5, 3.0))
   
    action_to_words = page.locator(
        PRACTICE_WORD_HUB_TAG, has_text=PRACTICE_WORD_HUB_TAG_INNER_TEXT
    )
    print("Button practice word finded...")
    await action_to_words.scroll_into_view_if_needed()
    print("Scrolled to button...")
    await action_to_words.click()
    print("Succesfully complete")
