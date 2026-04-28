import sqlite3
from .database import get_db

class Setting:
    """
    系統設定 Model
    """
    @classmethod
    def get(cls, key: str, default=None):
        """
        根據 Key 取得設定值，若無則回傳 default
        :param key: 設定鍵值
        :param default: 預設值
        """
        try:
            with get_db() as db:
                cursor = db.execute('SELECT value FROM settings WHERE key = ?', (key,))
                row = cursor.fetchone()
                return row['value'] if row else default
        except sqlite3.Error as e:
            print(f"Error in Setting.get: {e}")
            return default

    @classmethod
    def set(cls, key: str, value: str):
        """
        設定 Key-Value (若已存在則更新)
        :param key: 設定鍵值
        :param value: 設定內容
        """
        try:
            with get_db() as db:
                db.execute(
                    'INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value',
                    (key, str(value))
                )
                db.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error in Setting.set: {e}")
            return False
