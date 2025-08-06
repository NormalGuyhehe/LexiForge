from pathlib import Path
from core.generator.obsidian_module.structure.get_all_patritions import get_mount_points
from functools import lru_cache

@lru_cache
def find_obsidian_vaults():
    vaults = []
    for mount in get_mount_points():
        root = Path(mount)
        try:
            for path in root.rglob('Главная'):
                if path.is_dir():
                    vaults.append(path.parent)
                    print(f"[+] Найден Vault: {path.parent}")
        except PermissionError:
            print(f"[!] Нет доступа к: {root}")
    return vaults