# main.py
import asyncio
from functools import lru_cache
from core.duolingo.duolingo import get_data
from utils.user.write_user_data import write
from utils.user.have_user_data import have_data
from core.generator.manager import manager_orchestrator


@lru_cache
async def main() -> None:
    """Main script (will be updated more that once)
    v.0.1, Main feature in develop :
    - get words from Duolingo Dictionary ✔
    - split words and step-by-step query on OpenAI web-site with prompt
    - async write into cards and vault beetwen OpenAI requests
    """
    print("Starts of LexiForge...")
    if have_data:
        print("Start scraping duolingo...")
        await get_data()

        print("Finish scraping duolingo...")
        await manager_orchestrator()
    else:
        await write()
        await get_data()
        await manager_orchestrator()


if __name__ == "__main__":
    asyncio.run(main())
