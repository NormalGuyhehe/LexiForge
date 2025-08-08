from core.generator.Anki_module.anki_manager import anki_manager
from core.generator.obsidian_module.obsidian_manager import obsidian_manager
from functools import lru_cache


@lru_cache
async def manager_orchestrator():
    await obsidian_manager()
    await anki_manager()
