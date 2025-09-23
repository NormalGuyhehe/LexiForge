import asyncio
from pathlib import Path
from core.generator.LLM_module.engine.launch_powershell import run_powershell_module
from core.generator.LLM_module.engine.CDP_connect import CDP_connect_module
from core.generator.LLM_module.engine.get_debugging_url import get_debugging_cdp_url
from core.generator.LLM_module.engine.create_target import create_target
from core.generator.LLM_module.engine.attach_to_target import attach_to_target
from core.generator.LLM_module.engine.click_to_text_form import click_to_text_form
from core.generator.LLM_module.engine.typing_in_form import typing_to_form
from core.generator.LLM_module.engine.enter_responce_to_server import (
    enter_responce_to_server,
)

from core.generator.LLM_module.engine.get_answer import get_answer
from core.generator.LLM_module.engine.reload_page import reload_page
from core.generator.LLM_module.engine.to_chatgpt import walk_to_chatgpt

async def connect_llm(default_word: str, vocabulary_note_prompt: str, ROOT_DIRECTORY: Path):
    vocabulary_prompt = vocabulary_note_prompt.format(word=default_word)
    await run_powershell_module(ROOT_DIRECTORY)
    await asyncio.sleep(2)
    async with CDP_connect_module(get_debugging_cdp_url) as connection:
        target_id: str = await create_target(connection)
        print(target_id)
        session_id: str = await attach_to_target(connection, target_id)
        await asyncio.sleep(2)
        await walk_to_chatgpt(connection, session_id)
        await asyncio.sleep(2)
        await click_to_text_form(connection, session_id)
        await asyncio.sleep(2)
        await typing_to_form(connection, session_id, vocabulary_prompt)
        await asyncio.sleep(2)
        await enter_responce_to_server(connection, session_id)
        await asyncio.sleep(2)
        answer_from_server: str = await get_answer(connection, session_id)
        await reload_page(connection, session_id)
        return answer_from_server
