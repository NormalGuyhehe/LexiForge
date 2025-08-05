from core.generator.obsidian_module.structure_builder import structure_creator
from core.generator.obsidian_module.notes_writer import notes_writer
from core.generator.obsidian_module.obsidian_main_writer import main_writer
from functools import lru_cache

@lru_cache
async def obsidian_manager():
    print("all works")
    await structure_creator()
    # await main_writer()
    # await notes_writer()