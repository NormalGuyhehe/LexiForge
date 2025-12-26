import subprocess
from pathlib import Path
from utils.paths import get_root_path
from utils.take_anki_cards import take_anki_cards
from core.generator.LLM_module.LLM_manager import connect_llm
from core.generator.Anki_module.anki_up import anki_up
from core.generator.Anki_module.anki_writer import anki_api
from core.generator.Anki_module.anki_close import anki_close
from core.db.read_batch import read_batch_db

async def anki_manager():
    """Асинхронная функция для управления процессом создания карточек в Anki"""
    anki_cards_prompt: str = await take_anki_cards()
    ROOT_DIRECTORY: Path = get_root_path()
    expression: list = await read_batch_db()
    print(f" substracted from database{expression}")
    print("anki module works...")
    raw_expression: tuple = expression[0]
    expression_to_anki: str = raw_expression[1]
    PID: subprocess.Popen = await anki_up()
    for word in expression_to_anki.split(' '):
        anki_cards_text: str = await connect_llm(
            word, anki_cards_prompt, ROOT_DIRECTORY
        )
        front_side: str = anki_cards_text.split(";")[0].strip()
        back_side: str = anki_cards_text.split(";")[1].strip()
        await anki_api(front_side, back_side)
    await anki_close(PID)
    print("vocabulary card has been writed...")