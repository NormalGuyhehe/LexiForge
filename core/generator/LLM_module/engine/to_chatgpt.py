import json
from websockets.legacy.client import WebSocketClientProtocol


async def walk_to_chatgpt(connection: WebSocketClientProtocol, session_id: str):
    await connection.send(
        json.dumps(
            {
                "id": 456,
                "sessionId": session_id,
                "method": "Page.navigate",
                "params": {"url": "https://chatgpt.com"},
            }
        )
    )
    await connection.recv()
