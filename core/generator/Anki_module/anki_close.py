import subprocess, psutil
import asyncio
async def anki_close(PID: subprocess.Popen):
    """Асинхронная функция для закрытия Anki после завершения работы с ним"""
    parent = psutil.Process(PID.pid)
    await asyncio.sleep(5)  # Ждем 5 секунд перед закрытием Anki
    for child in parent.children(recursive=True):
        if child.is_running():
            print("Closing child process:", child)
            child.kill()
    print("Closing parent process:", parent)
    parent.kill()
    print("Anki закрыт.")