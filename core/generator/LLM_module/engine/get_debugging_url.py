import asyncio
import json
import requests
async def get_debugging_cdp_url():
    responce = requests.get("http://localhost:9222/json/version")
    rezult: dict = json.loads(responce.text)
    CDP_url: str = rezult["webSocketDebuggerUrl"]
    return CDP_url