// background.js
/// @ts-check
/// <reference lib="dom"/>
/// <reference lib="es2024"/>

chrome.runtime.onMessage.addListener((message) => {
    handleMessage(message);
    return true;
});

async function handleMessage(message) {
    const url = message.url;
    
    switch (message.type) {
        case "YOUTUBE_VIDEO_LINK":
            console.log("==========================================");
            console.log("Be released in the new Lexi Forge Browser Extension!");
            console.log(`✅ YOUTUBE LINK CAPTURED: ${url}`);
            console.log(`Видео ссылка: ${message.link}`);
            console.log("==========================================");
            break;

        case "SCRAPED_DATA":
            console.log("------------------------------------------");
            console.log(`🔎 SCRAPED DATA FOUND on: ${url}`);
            console.log(`Элемент-источник: <${message.elementTag}>`);
            console.log(`Найдено совпадений: ${message.matches?.length || 0}`);

            if (!Array.isArray(message.matches) || message.matches.length === 0) {
                console.warn("Нет совпадений для обработки.");
                return;
            }

            for (const match of message.matches) {
                console.log(`Информация/лексика : "${match.trim().substring(0, 100)}"`);
                try {
                    const response = await fetch("http://127.0.0.1:8000/get_lexical", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            match: match.trim().substring(0, 100)
                        })
                    });
                    const data = await response.json();
                    console.log("Ответ от сервера:", data.Rezult);
                } catch (err) {
                    console.error("Ошибка при запросе:", err);
                }
            }
            console.log("------------------------------------------");
            break;

        default:
            console.warn("Неизвестный тип сообщения:", message.type);
    }
}