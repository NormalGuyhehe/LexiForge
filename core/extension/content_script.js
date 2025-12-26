"use strict";
// @ts-check

// --- 1. Конфигурация ---
let lastUrl = location.href;

// МАКСИМАЛЬНО ШИРОКИЙ REGEX для латинского текста: 
// Ищет последовательность из 15 или более символов (латиница, цифры, пробелы и пунктуация).
/** @type {RegExp} */
const general_scan_regex = /\b(?:[A-Za-z]{3,}\s){2,}[A-Za-z]{3,}\b/g;;


// --- 2. Функции Обмена Сообщениями и Обработки ---

function sendMessageToBackground(message) {
    // В этом режиме просто отправляем сообщение, не ожидая ответа API
    try {
        chrome.runtime.sendMessage(message);
    } catch (e) {
        console.warn("Не удалось отправить сообщение в Background Script.");
    }
}

/**
 * Логика обработки изменения URL (только для YouTube).
 * @param {string} newUrl
 */
function handleUrlChange(newUrl) {
    
    if (newUrl.includes('youtube.com/watch')) {
        try {
            const urlObj = new URL(newUrl);
            const videoId = urlObj.searchParams.get("v");
            const finalLink = `https://www.youtube.com/watch?v=${videoId}`;
            
            sendMessageToBackground({
                type: "YOUTUBE_VIDEO_LINK",
                link: finalLink,
                url: newUrl
            });
        } catch (e) {
            console.error("Ошибка парсинга URL YouTube:", e);
        }
    }
}

/**
 * Функция для сканирования контента и отправки совпадений.
 * @param {Node} node
 */
function scanContent(node) {
    if (node.nodeType === Node.ELEMENT_NODE) {
        // Проверяем, что элемент не является скриптом или стилем
        if (node.tagName === 'SCRIPT' || node.tagName === 'STYLE') return;

        const fullText = (/** @type {HTMLElement} */ node).textContent || '';
        
        // Используем максимально широкий RegEx
        const matches = [...fullText.matchAll(general_scan_regex)]; 

        if (matches.length > 0) {
            sendMessageToBackground({
                type: "SCRAPED_DATA",
                matches: matches.map(m => m[0]),
                elementTag: node.tagName,
                url: location.href
            });
        }
    }
}


// --- 3. Mutation Observers и Инициализация ---

// Детектор Смены URL (Trigger навигации)
const url_change_detector = new MutationObserver(mutations => {
    if (location.href !== lastUrl) {
        lastUrl = location.href;
        handleUrlChange(lastUrl);
    }
});

// Сканер Контента (Непрерывный скрейпинг)
const content_scanner = new MutationObserver((mutationsList) => {
    for (const mutation of mutationsList) {
        // Ловим добавленные узлы (динамический контент)
        if (mutation.type === "childList" && mutation.addedNodes.length > 0) {
            mutation.addedNodes.forEach(node => {
                scanContent(node);
            });
        }
        // Ловим изменения в текстовом содержимом
        else if (mutation.type === "characterData") {
            scanContent(mutation.target.parentElement || mutation.target);
        }
    }
});


// --- 4. Запуск ---

const rootNode = document.documentElement;

if (rootNode) {
    console.log("Контент-скрипт активирован.");
    
    const observerConfig = { childList: true, subtree: true, characterData: true };

    url_change_detector.observe(rootNode, { childList: true, subtree: true });
    content_scanner.observe(rootNode, observerConfig);
    
    // 1. Обрабатываем URL при первой загрузке страницы
    handleUrlChange(location.href);

    // 2. ПЕРВОНАЧАЛЬНОЕ СКАНИРОВАНИЕ ВСЕГО СУЩЕСТВУЮЩЕГО КОНТЕНТА
    scanContent(rootNode); 
    console.log("Выполнено первоначальное сканирование всего документа.");
}