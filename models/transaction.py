from dataclasses import dataclass
from typing import Optional
from .database import get_db

@dataclass
class Transaction:
    id: int
    amount: float
    type: str
    category_id: int
    date: str
    note: Optional[str]
    created_at: str

    @classmethod
    def get_all(cls):
        with get_db() as db:
            cursor = db.execute('SELECT * FROM transactions ORDER BY date DESC, id DESC')
            return [cls(**row) for row in cursor.fetchall()]

    @classmethod
    def get_by_id(cls, tx_id: int):
        with get_db() as db:
            cursor = db.execute('SELECT * FROM transactions WHERE id = ?', (tx_id,))
            row = cursor.fetchone()
            return cls(**row) if row else None

    @classmethod
    def get_by_date_range(cls, start_date: str, end_date: str):
        with get_db() as db:
            cursor = db.execute(
                'SELECT * FROM transactions WHERE date >= ? AND date <= ? ORDER BY date DESC, id DESC',
                (start_date, end_date)
            )
            return [cls(**row) for row in cursor.fetchall()]

    @classmethod
    def create(cls, amount: float, tx_type: str, category_id: int, date: str, note: str = ""):
        with get_db() as db:
            cursor = db.execute(
                'INSERT INTO transactions (amount, type, category_id, date, note) VALUES (?, ?, ?, ?, ?)',
                (amount, tx_type, category_id, date, note)
            )
            db.commit()
            return cursor.lastrowid

    @classmethod
    def delete(cls, tx_id: int):
        with get_db() as db:
            db.execute('DELETE FROM transactions WHERE id = ?', (tx_id,))
            db.commit()
            return True
