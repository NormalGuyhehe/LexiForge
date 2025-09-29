from core.generator.Anki_module.anki_manager import anki_manager
from core.generator.obsidian_module.obsidian_manager import obsidian_manager
from functools import lru_cache


@lru_cache
async def manager_orchestrator():
    print("obsidian (.md ) manager started...")
    # await obsidian_manager()
    # print("obsidian (.md ) manager finished...")
    # print("Anki manager started...")
    await anki_manager()
    print("Anki process finished...")
    print("LexiForge finished completely")