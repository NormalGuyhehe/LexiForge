import json
import random
from websockets.legacy.client import WebSocketClientProtocol


async def reload_page(connection: WebSocketClientProtocol, session_id: str):
    await connection.send(
        json.dumps(
            {
                "id": random.randint(1000, 9999),
                "method": "Page.reload",
                "params": {"ignoreCache": True},
                "sessionId": session_id
            }
        )
    )
    await connection.recv()
