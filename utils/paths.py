from pathlib import Path
async def get_root_path():
    ROOT_PATH: Path = Path(__file__).resolve().parents[1]
    return ROOT_PATH