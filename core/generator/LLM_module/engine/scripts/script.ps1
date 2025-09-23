$chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$userdatadir = "C:\Users\GreatLord\AppData\Local\Google\Chrome\User Data\Default"
$port = 9222

# Оптимизированные параметры запуска Chrome
$chromeArgs = @(
    "--remote-debugging-port=$port",
    "--user-data-dir=`"$userdatadir`"",
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-background-timer-throttling",      # Предотвращает замедление таймеров в фоновых вкладках
    "--disable-backgrounding-occluded-windows",   # Предотвращает снижение приоритета для скрытых окон
    "--disable-renderer-backgrounding",           # Отключает фоновое понижение приоритета рендерера
    "--disable-dev-shm-usage",                    # Избегает использование /dev/shm (полезно в некоторых окружениях)
    "--no-zygote",                                # Отключает использование zygote процесса (снижает потребление памяти)
    "--disable-gpu",                              # Отключает аппаратное ускорение (если не нужно)
    "--disable-software-rasterizer",              # Отключает софтверный растеризатор
    "--disable-extensions",                       # Отключает расширения (если они не нужны)
    "--disable-sync",                             # Отключает синхронизацию
    "--disable-default-apps",                     # Отключает стандартные приложения
    "--disable-translate",                        # Отключает переводчик
    "--metrics-recording-only",                   # Только запись метрик (снижает нагрузку)
    "--no-default-browser-check",                 # Уже было, но оставляем
    "--headless-new"
)

# Проверяем, занят ли порт 9222 и является ли процесс Chrome
$portProcess = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue |
    ForEach-Object { Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue } |
    Where-Object { $_.ProcessName -eq "chrome" }

if ($portProcess) {
    Write-Host "Chrome уже запущен на порту $port (PID: $($portProcess.Id))"
} else {
    # Запуск Chrome с оптимизированными параметрами
    $process = Start-Process -FilePath $chromepath -PassThru -ArgumentList $chromeArgs
    
    # Дать время Chrome запуститься и привязать порт
    Start-Sleep -Seconds 3

    # Проверяем, успешно ли запустился процесс и слушает порт
    $portCheck = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue |
        Where-Object { $_.OwningProcess -eq $process.Id }

    if ($portCheck) {
        Write-Host "Chrome запущен на порту $port (PID: $($process.Id)) с оптимизированными параметрами"
    } else {
        Write-Warning "Процесс Chrome запущен (PID: $($process.Id)), но порт $port не слушается. Возможно, произошла ошибка."
    }
}