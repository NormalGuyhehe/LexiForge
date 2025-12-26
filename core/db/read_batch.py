import aiosqlite

async def read_batch_db(batch_quantity: int = 1) -> dict:
    async with aiosqlite.connect("core/db/lexical.db") as db:
        async with db.execute("BEGIN") as cursor:
            cursor = await db.execute("""
                SELECT id, expression
                FROM lexical_info
                WHERE status = 'new'
                ORDER BY created_at
                LIMIT ?
            """, (batch_quantity,   )
            )
            rows = await cursor.fetchall()
            ids = [row[0]  for row in rows]
            
            if ids:
                await db.executemany("""
                    UPDATE lexical_info
                    SET status = 'processing'
                    WHERE id = ?
                """, [(i, ) for i in ids])
                await db.commit()
        return rows