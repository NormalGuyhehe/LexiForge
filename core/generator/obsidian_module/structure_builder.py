from pathlib import *
from functools import lru_cache
from core.generator.obsidian_module.structure.find_obsidian_vaults import find_obsidian_vaults
from core.generator.obsidian_module.structure.language_structure import *
@lru_cache
async def structure_creator():
    vault_list = find_obsidian_vaults()
    for vault in vault_list:
        if (
            vault.is_dir and 
            vault.name == "Главная" and
            vault.parent.name == ".obsidian"
            ):
            for folder in directories:
                path = vault / folder
                # path.   