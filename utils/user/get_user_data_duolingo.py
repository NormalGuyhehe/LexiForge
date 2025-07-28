import os
def take_user_data_duolingo() -> list[str, str]:
    email: str = os.getenv("DUOLINGO_USERNAME")
    password: str = os.getenv("DUOLINGO_PASSWORD")
    return [email, password]