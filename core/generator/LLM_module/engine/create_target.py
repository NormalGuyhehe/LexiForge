import json
from websockets.legacy.client import WebSocketClientProtocol


async def create_target(ws: WebSocketClientProtocol):
    await ws.send(
        json.dumps(
            {
                "id": 1,
                "method": "Target.getTargets",
                "params": {"url": "https://chat.openai.com/chat"},
            }
        )
    )
    response: dict = json.loads(await ws.recv())
    target_id: str = next(
        (
            item["targetId"]
            for item in response["result"]["targetInfos"]
            if item["type"] == "page"
        ),
        None,
    )
    return target_id