# import asyncio
# import random
# import json
# from websockets.legacy.client import WebSocketClientProtocol
# async def get_answer(connection: WebSocketClientProtocol, session_id: str):
#     for _ in range(10):
#             await connection.send(
#                 json.dumps(
#                     {
#                         "id": random.randint(1000, 9999),
#                         "method": "Runtime.evaluate",
#                         "sessionId": session_id,
#                         "params": {
#                             "expression": """
#                 (() => {
#                     const messages = document.querySelectorAll('article[data-turn="assistant"] .markdown.prose');
#                     const last = messages[messages.length - 1];
#                     return last ? last.innerText : '';
#                 })()
#                 """,
#                             "returnByValue": True,
#                         },
#                     }
#                 )
#             )
#             response = await connection.recv()
#             result: dict = json.loads(response)
#             check_value: dict = result.get("result", {}).get("result", {})
#             if check_value.get("type") != "undefined" and check_value.get("value"):
#                 print(check_value)

import asyncio
import json
from websockets.legacy.client import WebSocketClientProtocol

async def get_answer(connection: WebSocketClientProtocol, session_id: str):
    previous_text = None
    full_text = ""
    stable_count = 0
    required_stable_cycles = 3  # сколько раз подряд текст должен быть неизменным

    while True:
        # Отправляем запрос в Runtime.evaluate, читаем последний ответ ассистента из DOM
        await connection.send(json.dumps({
            "id": 1,
            "method": "Runtime.evaluate",
            "sessionId": session_id,
            "params": {
                "expression": """
(() => {
    const messages = document.querySelectorAll('article[data-turn="assistant"] .markdown.prose');
    const last = messages[messages.length - 1];
    return last ? last.innerText : '';
})()
""",
                "returnByValue": True,
            }
        }))

        # Ждём ответ
        response = await connection.recv()
        result: dict = json.loads(response)
        value = result.get("result", {}).get("result", {}).get("value", "")

        if not value:
            await asyncio.sleep(0.1)
            continue

        full_text = value

        # Проверяем, изменился ли текст
        if full_text == previous_text:
            stable_count += 1
        else:
            stable_count = 0  # сброс, если текст обновился

        previous_text = full_text

        # Если текст стабилен required_stable_cycles циклов подряд — считаем его финальным
        if stable_count >= required_stable_cycles:
            break

        # Маленькая пауза, чтобы DOM успел обновиться
        await asyncio.sleep(0.1)

    print("Responce from server: ", full_text)
    return full_text
