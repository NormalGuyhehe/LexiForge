import aiosqlite


async def initialize_db(db_path: str) -> None:
    """Initialize the database with required tables."""
    async with aiosqlite.connect(db_path) as db:
        print("Initializing the database...")
        await db.execute("""
                CREATE TABLE IF NOT EXISTS lexical_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                batch_id TEXT NOT NULL,
                expression TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'new',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(batch_id, expression)
            )
        """)
        print("words table ensured.")
        await db.commit()
        print("Database initialized.")
