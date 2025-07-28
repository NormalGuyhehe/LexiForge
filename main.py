# main.py
import os
import time
from core.duolingo.load_page import get_page
from utils.user.write_user_data import write
from utils.user.validate_user_data import validate_data
def main() -> None:
    """Main script (will be updated more that once)
    v.0.1, Main feature in develop : 
    - get words from Duolingo Dictionary 
    - split words and step-by-step query on OpenAI web-site with prompt
    """
    if validate_data():  
        get_page()
    else:
        write()
if __name__ == "__main__":
    main()