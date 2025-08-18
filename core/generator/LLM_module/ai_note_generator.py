import asyncio
import random
from playwright.async_api import Page


async def note_generator(openAI: Page, default_word, translate):
    print("go to bing...")
    await openAI.goto("https://www.bing.com")
    await asyncio.sleep(2)
    print("Succesfuly...")
    print("Finds a Copilot button...")
    await asyncio.sleep(2)
    go_to_AI = openAI.locator('button[part="control"]', has_text="Copilot")
    print("Copilot button finded...")
    await asyncio.sleep(2)
    await go_to_AI.click(force=True)
    print("Click a Copilot button...")
    await asyncio.sleep(2)
    # text_area = openAI.locator("textarea")
    # await text_area.click(force=True)
    # await text_area.fill("что нибудь")
    await asyncio.sleep(10)
    # submit_button = openAI.locator('[data-testid="submit-button"]')
    # await submit_button.click(force=True)
    # await asyncio.sleep(3)
    # get_language_answer = openAI.locator('[class="group/ai-message-item space-y-3 break-words"]').all_inner_texts()
    # print(get_language_answer)
    # prompt_area = openAI.locator('[data-placeholder="Спросите что-нибудь…"]')
    # await prompt_area.fill("что нибудь", force=True)
    # fetch_button = openAI.locator('[data-testid="send-button"]')
    # await fetch_button.click(force=True)