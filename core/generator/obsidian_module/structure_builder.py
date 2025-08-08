import os
from pathlib import Path
from functools import lru_cache
from core.generator.obsidian_module.structure.find_obsidian_vaults import (
    find_obsidian_vaults,
)
from core.generator.obsidian_module.structure.language_structure import *


@lru_cache
async def structure_creator():
    vault_list: Path = find_obsidian_vaults()
    for vault in vault_list:
        if (
            vault.is_dir
            and vault.name == "obsidian"
            and vault.parent.name == "Documents"
        ):
            path_to_main = vault / "Главная"
            os.chdir(str(path_to_main))
            path_to_english_folder = path_to_main / "english"
            os.chdir("english")
            if (
                Path("vocabulary").is_dir()
                and Path("grammarly").is_dir()
                and Path("anki_cards").is_dir()
            ):
                print(
                    "Container for words notes/grammarly notes/anki cards is exists, good to work..."
                )
                return path_to_english_folder
            else:
                vocabulary_folder: Path = Path("vocabulary")
                vocabulary_folder.mkdir()
                print("Make a vocabulary directory")
                grammarly_folder: Path = Path("grammarly")
                grammarly_folder.mkdir()
                print("Make a grammarly directory")
                anki_folder: Path = Path("anki_cards")
                anki_folder.mkdir()
                print("Make an anki_folder directory")
                current_directory = os.getcwd()
                os.listdir(current_directory)
                return path_to_english_folder
