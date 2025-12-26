from core.generator.obsidian_module.structure_builder import structure_creator
from core.generator.obsidian_module.obsidian_main_writer import main_writer
from core.generator.obsidian_module.notes_writer import words_notes_writer
from core.generator.obsidian_module.grammarly_writer import grammarly_writer
from utils.paths import get_root_path


async def obsidian_manager():
    print("Starts create files and directory...")
    ROOT_DIRECTORY: str = get_root_path()
    print(ROOT_DIRECTORY)
    print("Get current directory...")
    structure_creator(ROOT_DIRECTORY)
    print("Create folder and files structure...")
    main_writer(ROOT_DIRECTORY)
    print("Create main language file...")
    await words_notes_writer(ROOT_DIRECTORY)
    print("Writed all vocabulary notes...")
    grammarly_writer(ROOT_DIRECTORY)
    print("Writed all grammarly notes...")
    print("ALL NOTES WROTES...")
