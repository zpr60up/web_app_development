import sqlite3
from dataclasses import dataclass
from typing import Optional
from .database import get_db

@dataclass
class Transaction:
    """
    收支明細 Model
    """
    id: int
    amount: float
    type: str
    category_id: int
    date: str
    note: Optional[str]
    created_at: str

    @classmethod
    def get_all(cls):
        """取得所有收支明細，依日期與 ID 遞減排序"""
        try:
            with get_db() as db:
                cursor = db.execute('SELECT * FROM transactions ORDER BY date DESC, id DESC')
                return [cls(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error in Transaction.get_all: {e}")
            return []

    @classmethod
    def get_by_id(cls, tx_id: int):
        """根據 ID 取得單筆收支明細"""
        try:
            with get_db() as db:
                cursor = db.execute('SELECT * FROM transactions WHERE id = ?', (tx_id,))
                row = cursor.fetchone()
                return cls(**row) if row else None
        except sqlite3.Error as e:
            print(f"Error in Transaction.get_by_id: {e}")
            return None

    @classmethod
    def get_by_date_range(cls, start_date: str, end_date: str):
        """
        取得指定日期區間的收支明細
        :param start_date: 起始日期 (YYYY-MM-DD)
        :param end_date: 結束日期 (YYYY-MM-DD)
        """
        try:
            with get_db() as db:
                cursor = db.execute(
                    'SELECT * FROM transactions WHERE date >= ? AND date <= ? ORDER BY date DESC, id DESC',
                    (start_date, end_date)
                )
                return [cls(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error in Transaction.get_by_date_range: {e}")
            return []

    @classmethod
    def create(cls, data: dict):
        """
        建立一筆新收支明細
        :param data: 包含 amount, type, category_id, date, note 的字典
        """
        try:
            with get_db() as db:
                cursor = db.execute(
                    'INSERT INTO transactions (amount, type, category_id, date, note) VALUES (?, ?, ?, ?, ?)',
                    (data.get('amount'), data.get('type'), data.get('category_id'), data.get('date'), data.get('note', ''))
                )
                db.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error in Transaction.create: {e}")
            return None

    @classmethod
    def update(cls, tx_id: int, data: dict):
        """
        更新單筆收支明細
        :param tx_id: 明細 ID
        :param data: 要更新的資料字典
        """
        try:
            with get_db() as db:
                db.execute(
                    'UPDATE transactions SET amount = ?, type = ?, category_id = ?, date = ?, note = ? WHERE id = ?',
                    (data.get('amount'), data.get('type'), data.get('category_id'), data.get('date'), data.get('note', ''), tx_id)
                )
                db.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error in Transaction.update: {e}")
            return False

    @classmethod
    def delete(cls, tx_id: int):
        """
        刪除單筆收支明細
        :param tx_id: 明細 ID
        """
        try:
            with get_db() as db:
                db.execute('DELETE FROM transactions WHERE id = ?', (tx_id,))
                db.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error in Transaction.delete: {e}")
            return False
