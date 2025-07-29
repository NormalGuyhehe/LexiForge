import os
from dotenv import load_dotenv
def have_data() -> bool:
    """Проверяет наличие логина и пароля"""
    load_dotenv()
    if os.path.exists(".env") and "DUOLINGO_USERNAME" in os.environ and "DUOLINGO_PASSWORD" in os.environ:
        return True