from asyncio import Queue
from core.generator.anki.anki_manager import anki_manager
from core.generator.obsidian.obsidian_manager import obsidian_manager
from utils.data.get_words import get_dictionary_from_file
async def manager_orchestrator():
    data_set = await get_dictionary_from_file()
    workers = Queue(maxsize=5)
    await workers.put(obsidian_manager)
    await workers.put(anki_manager)