import os
from functools import lru_cache

@lru_cache
def return_anki_path(filename="anki.exe", search_path="C:\\"): # Для Linux/Mac используй "/"
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            full_path = os.path.join(root, filename)
            if os.access(full_path, os.X_OK):
                print("Executable Anki file is exists")
                return full_path
    print("executable file of Anki not exists")
    return None