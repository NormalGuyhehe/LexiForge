import websockets
import json
async def take_cdp_session(debugger_url: str):
    async with websockets.connect(debugger_url) as ws:
        await ws.send(
            json.dumps(
                {
                    "id": 1,
                    "method": "Target.createTarget",
                    "params": {"url": "https://chat.openai.com/chat"},
                }
            )
        )
        response: dict = json.loads(await ws.recv())
        target_id: str = response["result"]["targetId"]
        print("Target ID:", target_id)