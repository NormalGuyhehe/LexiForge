from pathlib import Path
from core.db.read_batch import read_batch_db
from utils.take_vocabulay_prompt import take_vocabulary_prompt
from core.generator.LLM_module.LLM_manager import connect_llm


async def words_notes_writer(ROOT_DIRECTORY: Path):
    expression: list = await read_batch_db()
    print(f" substracted from database{expression}")
    print("notes module works...")
    vocabulary_note_prompt: str = take_vocabulary_prompt()
    raw_expression: tuple = expression[0]
    expression_to_words: str = raw_expression[1]
    for word in expression_to_words.split(' '):
        target_to_write: Path = Path("english") / "vocabulary" / f"{word}.md"
        vocabulary_note_text: str = await connect_llm(
            word, vocabulary_note_prompt, ROOT_DIRECTORY
        )
        target_to_write.write_text(vocabulary_note_text, encoding="utf-8")
    print("vocabulary note has been writed...")