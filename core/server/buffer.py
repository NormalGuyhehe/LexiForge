import asyncio
import time

buffer: list = []
lock = asyncio.Lock()
last_flush = time.time()

MAX_SIZE = 1000
MAX_AGE = 2.0