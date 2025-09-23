import json
import asyncio
import random


async def click_to_text_form(connection, session_id: str):
    await connection.send(
        json.dumps(
            {
                "id": random.randint(10, 99999),
                "method": "Runtime.evaluate",
                "sessionId": session_id,
                "params": {
                    "expression": """
                const observer = new MutationObserver(() => {
                  const btn = document.querySelector('a.text-token-text-secondary.underline');
                  if (btn) {
                    btn.click();
                    observer.disconnect();
                    console.log("succesfully'");
                  }
                });
                observer.observe(document.body, { childList: true, subtree: true });
                """
                },
            }
        )
    )
    response = json.loads(await connection.recv())
    print("Responce text:", response)
    await asyncio.sleep(2)
