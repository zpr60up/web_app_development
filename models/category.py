from dataclasses import dataclass
from .database import get_db

@dataclass
class Category:
    id: int
    name: str
    type: str
    is_default: bool

    @classmethod
    def get_all(cls):
        with get_db() as db:
            cursor = db.execute('SELECT * FROM categories ORDER BY type, id')
            return [cls(**row) for row in cursor.fetchall()]

    @classmethod
    def get_by_id(cls, cat_id: int):
        with get_db() as db:
            cursor = db.execute('SELECT * FROM categories WHERE id = ?', (cat_id,))
            row = cursor.fetchone()
            return cls(**row) if row else None

    @classmethod
    def create(cls, name: str, cat_type: str):
        with get_db() as db:
            cursor = db.execute(
                'INSERT INTO categories (name, type, is_default) VALUES (?, ?, 0)',
                (name, cat_type)
            )
            db.commit()
            return cursor.lastrowid

    @classmethod
    def delete(cls, cat_id: int):
        with get_db() as db:
            # Prevent deleting default categories
            cursor = db.execute('SELECT is_default FROM categories WHERE id = ?', (cat_id,))
            row = cursor.fetchone()
            if not row or row['is_default']:
                return False
            db.execute('DELETE FROM categories WHERE id = ?', (cat_id,))
            db.commit()
            return True
