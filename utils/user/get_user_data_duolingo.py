import os
from dotenv import load_dotenv
def take_user_data_duolingo() -> list[str, str]:
    load_dotenv()
    email: str = os.getenv("DUOLINGO_USERNAME")
    password: str = os.getenv("DUOLINGO_PASSWORD")
    return [email, password]