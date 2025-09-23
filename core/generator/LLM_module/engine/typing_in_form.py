import json
from websockets.legacy.client import WebSocketClientProtocol


async def typing_to_form(
    connection: WebSocketClientProtocol, session_id: str, vocabulary_prompt: str
):
    # Безопасно сериализуем текст для JS
    safe_text = json.dumps(vocabulary_prompt)

    expression = f"""
(function typeInProseMirror(text) {{
    const maxTries = 50;
    const delay = 200;
    let tries = 0;

    function checkEl() {{
        const el = document.querySelector('.ProseMirror');
        if (!el) {{
            if (tries++ < maxTries) setTimeout(checkEl, delay);
            else console.log('ProseMirror не найден');
            return;
        }}

        el.focus();

        // Вводим текст по символам
        for (let char of text) {{
            el.dispatchEvent(new KeyboardEvent('keydown', {{ key: char, bubbles: true }}));
            el.dispatchEvent(new KeyboardEvent('keypress', {{ key: char, bubbles: true }}));
            el.textContent += char;  // чтобы визуально отображалось
            el.dispatchEvent(new Event('input', {{ bubbles: true }}));
            el.dispatchEvent(new KeyboardEvent('keyup', {{ key: char, bubbles: true }}));
        }}

        // Симулируем Enter
        el.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Enter', code: 'Enter', keyCode: 13, bubbles: true }}));
        el.dispatchEvent(new KeyboardEvent('keyup', {{ key: 'Enter', code: 'Enter', keyCode: 13, bubbles: true }}));

        console.log('Текст введён и Enter отправлен!');
    }}

    checkEl();
}})({safe_text});
"""

    await connection.send(
        json.dumps(
            {
                "id": 3,
                "method": "Runtime.evaluate",
                "sessionId": session_id,
                "params": {"expression": expression},
            }
        )
    )
    response = await connection.recv()
    print("Response:", response)
