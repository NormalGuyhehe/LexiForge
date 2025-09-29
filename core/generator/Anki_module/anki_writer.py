import aiohttp
import json


async def anki_api(front_side, back_side):
    """Асинхронная функция для создания простой карточки в Anki с полем ввода ответа"""
    note = {
        "deckName": "По умолчанию",
        "modelName": "Простая (с вводом ответа)",
        "fields": {"Front": front_side, "Back": back_side},
    }
    payload = {"action": "addNote", "version": 5, "params": {"note": note}}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://127.0.0.1:8765",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
            ) as response:
                result = await response.json()

                if result.get("error"):
                    print(f"Ошибка: {result['error']}")
                else:
                    print(f"Карточка успешно добавлена. ID: {result['result']}")

                return result

    except aiohttp.ClientError as e:
        print(f"Ошибка подключения к Anki: {e}")
        return None
