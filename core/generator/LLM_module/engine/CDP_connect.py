from contextlib import asynccontextmanager
import websockets

@asynccontextmanager
async def CDP_connect_module(debugger_url):
    CDP_url: str = await debugger_url()
    try:
        async with websockets.connect(CDP_url) as ws:
            print("CDP session create succesfully...")
            yield ws
    except Exception as e:
        print(f"Don`t worry, developers are fix this : {e}")
    finally:
        await ws.close()