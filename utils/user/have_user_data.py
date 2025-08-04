import os
from dotenv import load_dotenv
def have_data() -> bool:
    """Validate have login and password"""
    load_dotenv()
    print("Complete of loaded .env file(s)...")
    if os.path.exists(".env") and "DUOLINGO_USERNAME" in os.environ and "DUOLINGO_PASSWORD" in os.environ:
        print("Return user data complete...")
        return True