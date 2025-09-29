import subprocess
from subprocess import Popen
async def anki_up():
    """Function to open Anki application"""
    PID: Popen[bytes] = subprocess.Popen(["C://Users//GreatLord//AppData//Local//Programs//Anki//anki.exe"])
    print(f"Anki application opened, PID of process {PID.pid}...")
    return PID