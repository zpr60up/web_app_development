import sqlite3
from contextlib import contextmanager

DB_PATH = 'instance/database.db'
SCHEMA_PATH = 'database/schema.sql'

def init_db():
    """
    初始化資料庫。
    建立資料庫檔案與資料表，並載入預設的 schema。
    """
    import os
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with get_db() as db:
            if os.path.exists(SCHEMA_PATH):
                with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                    db.executescript(f.read())
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    except Exception as e:
        print(f"Error during db init: {e}")

@contextmanager
def get_db():
    """
    取得資料庫連線的 Context Manager。
    確保連線使用後會自動關閉。
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        yield conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()
