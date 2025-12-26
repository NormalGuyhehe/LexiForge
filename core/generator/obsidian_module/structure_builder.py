from functools import lru_cache
from pathlib import Path

@lru_cache
def structure_creator(ROOT_DIRECTORY):
    print(ROOT_DIRECTORY)
    middle_path: Path = Path(ROOT_DIRECTORY)
    english_path: Path = middle_path / "english"
    grammarly_path: Path = english_path / "grammarly"
    vocabulary_path: Path = english_path / "vocabulary"
    
    if english_path.exists():
        print("english folder already exists")
        if grammarly_path.exists() and vocabulary_path.exists():
            print("grammarly and vocabulary folder already exists")
    else:
        english_path.mkdir()
        grammarly_path.mkdir()
        vocabulary_path.mkdir()