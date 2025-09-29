from subprocess import Popen
from pathlib import Path
from utils.get_words import get_dictionary_from_file
from utils.paths import get_root_path
from utils.take_anki_cards import take_anki_cards
from core.generator.LLM_module.LLM_manager import connect_llm
from core.generator.Anki_module.anki_up import anki_up
from core.generator.Anki_module.anki_writer import anki_api
from core.generator.Anki_module.anki_close import anki_close


async def anki_manager():
    """Асинхронная функция для управления процессом создания карточек в Anki"""
    ROOT_DIRECTORY: Path = await get_root_path()
    words_dict_or_set: dict = await get_dictionary_from_file()
    print("anki module works...")
    anki_cards_prompt: str = await take_anki_cards()
    PID: Popen[bytes] = await anki_up()
    for default_word in words_dict_or_set.keys():
        anki_cards_text: str = await connect_llm(
            default_word, anki_cards_prompt, ROOT_DIRECTORY
        )
        front_side: str = anki_cards_text.split(";")[0].strip()
        back_side: str = anki_cards_text.split(";")[1].strip()
        await anki_api(front_side, back_side)
    await anki_close(PID)