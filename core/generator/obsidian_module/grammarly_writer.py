from pathlib import Path
from utils.get_words import get_dictionary_from_file
from utils.take_grammarly_prompt import take_grammarly_prompt
from core.generator.LLM_module.LLM_manager import connect_llm


async def grammarly_writer(ROOT_DIRECTORY: str):
    """This function writed only grammarly notes for every word"""
    words_dict_or_set: dict = await get_dictionary_from_file()
    print("grammarly notes module works...")
    vocabulary_note_prompt: str = await take_grammarly_prompt()
    for default_word in words_dict_or_set.keys():
        target_to_write: Path = Path("english") / "grammarly" / f"{default_word}.md"
        vocabulary_note_text: str = await connect_llm(
            default_word, vocabulary_note_prompt, ROOT_DIRECTORY
        )
        target_to_write.write_text(vocabulary_note_text, encoding="utf-8")
    print("process finished...")
