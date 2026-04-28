from .database import get_db

class Setting:
    @classmethod
    def get(cls, key: str, default=None):
        with get_db() as db:
            cursor = db.execute('SELECT value FROM settings WHERE key = ?', (key,))
            row = cursor.fetchone()
            return row['value'] if row else default

    @classmethod
    def set(cls, key: str, value: str):
        with get_db() as db:
            db.execute(
                'INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value',
                (key, str(value))
            )
            db.commit()
