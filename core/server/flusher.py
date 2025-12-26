import asyncio
import time
from uuid import uuid4
from core.server.buffer import buffer, lock, last_flush, MAX_SIZE, MAX_AGE
from core.db.write_db import write_lexical_db
from core.generator.obsidian_module.obsidian_manager import obsidian_manager
from core.generator.Anki_module.anki_manager import anki_manager
async def flusher():
    global last_flush

    while True:
        await asyncio.sleep(0.5)

        async with lock:
            if not buffer:
                continue

            if len(buffer) < MAX_SIZE and time.time() - last_flush < MAX_AGE:
                continue

            batch = buffer.copy()
            print(f"{len(batch)} items, full buffer: {buffer}")
            buffer.clear()
            last_flush = time.time()
       
        batch_id = str(uuid4())
        print(f"Flushing batch {batch_id} with {len(batch)} items, full buffer: {buffer}")
        await write_lexical_db(batch, batch_id)
        print("take data into pipeline")
        await anki_manager()
        # await obsidian_manager()