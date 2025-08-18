import os
from functools import lru_cache
from core.generator.obsidian_module.structure_builder import structure_creator
from core.generator.obsidian_module.obsidian_main_writer import main_writer
from core.generator.obsidian_module.notes_writer import words_notes_writer
from core.generator.obsidian_module.grammarly_writer import grammarly_writer

@lru_cache
async def obsidian_manager():
    print("Starts create files and directory...")
    current_dir = os.getcwd()
    print("Get current directory...")
    vault_path = await structure_creator(current_dir)
    print("Create folder and files structure...")
    await main_writer(vault_path)
    print("Create main language file...")
    await words_notes_writer(current_dir, vault_path)
    print("Writed all vocabulary notes...")
    await grammarly_writer(current_dir, vault_path)
    print("Writed all grammarly notes...")