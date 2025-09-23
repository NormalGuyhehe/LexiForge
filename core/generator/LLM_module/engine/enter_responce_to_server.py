import json
from websockets.legacy.client import WebSocketClientProtocol
async def enter_responce_to_server(connection: WebSocketClientProtocol, session_id):
    await connection.send(
            json.dumps(
                {
                    "id": 4,
                    "method": "Runtime.evaluate",
                    "params": {
                        "expression": """
                            (function(){
                                const btn = document.querySelector('#composer-submit-button');
                                if (btn){
                                    btn.click();
                                    true;
                                }
                                else{
                                    false;
                                }
                            })()
                        """,
                        "returnByValue": True,
                    },
                    "sessionId": session_id,
                }
            )
        )
    responce = await connection.recv()
    print("Reponce: ", responce)