from asyncio import Queue
from core.generator.obsidian.structure import structure_creator
from core.generator.obsidian.notes_writer import notes_writer
from core.generator.obsidian.obsidian_main_writer import main_writer
async def obsidian_manager():
    obsidian_queue = Queue() 
    await obsidian_queue.put(structure_creator)
    await obsidian_queue.put(notes_writer)
    await obsidian_queue.put(main_writer)