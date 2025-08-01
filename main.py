# main.py
import asyncio
from core.duolingo.duolingo import get_data
from utils.user.write_user_data import write
from utils.user.have_user_data import have_data
async def main() -> None:
    """Main script (will be updated more that once)
    v.0.1, Main feature in develop : 
    - get words from Duolingo Dictionary 
    - split words and step-by-step query on OpenAI web-site with prompt
    """
    print("Starts of LexiForge")
    if have_data:
        print("Start scraping duolingo")
        await get_data()
        print("Finish scraping duolingo")
    else:
        await write()
        await get_data()
if __name__ == "__main__":
    asyncio.run(main())