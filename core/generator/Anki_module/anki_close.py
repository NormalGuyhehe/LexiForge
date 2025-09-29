from subprocess import Popen
async def anki_close(PID: Popen[bytes]):
    """Асинхронная функция для закрытия Anki после завершения работы с ним"""
    PID.terminate()
    print("Anki закрыт.")
    return 0