# main.py
import asyncio
from core.duolingo.duolingo import get_data
from utils.user.write_user_data import write
from utils.user.have_user_data import have_data
from core.generator.manager import manager_orchestrator


async def main() -> None:
    """Main script (will be updated more that once)"""
    print("Starts of LexiForge...")
    if have_data():
        print("Start scraping duolingo...")
        # await get_data()

        print("Finish scraping duolingo...")
        await manager_orchestrator()
        print("Process finished...")
    else:
        await write()
        # await get_data()
        await manager_orchestrator()


if __name__ == "__main__":
    asyncio.run(main())
