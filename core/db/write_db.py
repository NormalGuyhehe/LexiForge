import aiosqlite

async def write_lexical_db(batch, batch_id):
    async with aiosqlite.connect("core/db/lexical.db") as db:
        unique_batch = list(set(batch))
        cursor = await db.cursor()
        await cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lexical_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                batch_id TEXT NOT NULL,
                expression TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'new',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(batch_id, expression)
            )
            """
        )
        await cursor.executemany(
            """
            INSERT OR IGNORE INTO lexical_info (batch_id, expression)
            VALUES (?, ?)
            """,
            [(batch_id, expression) for expression in unique_batch]
        )
        await db.commit()
        await cursor.close()