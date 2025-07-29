# main.py
from core.duolingo.get_data import get_data
from utils.user.write_user_data import write
from utils.user.have_user_data import have_data
def main() -> None:
    """Main script (will be updated more that once)
    v.0.1, Main feature in develop : 
    - get words from Duolingo Dictionary 
    - split words and step-by-step query on OpenAI web-site with prompt
    """
    if have_data:  
        get_data()
    else:
        write()
        get_data()
if __name__ == "__main__":
    main()