import subprocess
from utils.return_anki_path import return_anki_path
async def anki_up():
    """Function to open Anki application"""
    path_to_anki: str = return_anki_path()
    PID: subprocess.Popen = subprocess.Popen([f"{path_to_anki}"])
    print(f"Anki application opened, PID of process {PID.pid}...")
    return PID