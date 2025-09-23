import json
async def attach_to_target(connection, target_id: str):
    await connection.send(
        json.dumps(
                {
                    "id": 2,
                    "method": "Target.attachToTarget",
                    "params": {"targetId": target_id, "flatten": True},
                }
            )
        )
    response: dict = json.loads(await connection.recv())
    print("Attach:", response)
    session_id: str = response["params"]["sessionId"]
    return session_id