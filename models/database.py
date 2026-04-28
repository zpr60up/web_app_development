import sqlite3
from contextlib import contextmanager

DB_PATH = 'database/app.db'
SCHEMA_PATH = 'database/schema.sql'

def init_db():
    import os
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with get_db() as db:
        if os.path.exists(SCHEMA_PATH):
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                db.executescript(f.read())

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
