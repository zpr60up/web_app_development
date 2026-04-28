import sqlite3
from dataclasses import dataclass
from .database import get_db

@dataclass
class Category:
    """
    收支分類 Model
    """
    id: int
    name: str
    type: str
    is_default: bool

    @classmethod
    def get_all(cls):
        """取得所有收支分類"""
        try:
            with get_db() as db:
                cursor = db.execute('SELECT * FROM categories ORDER BY type, id')
                return [cls(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error in Category.get_all: {e}")
            return []

    @classmethod
    def get_by_id(cls, cat_id: int):
        """根據 ID 取得單筆分類"""
        try:
            with get_db() as db:
                cursor = db.execute('SELECT * FROM categories WHERE id = ?', (cat_id,))
                row = cursor.fetchone()
                return cls(**row) if row else None
        except sqlite3.Error as e:
            print(f"Error in Category.get_by_id: {e}")
            return None

    @classmethod
    def create(cls, data: dict):
        """
        建立新的自訂分類
        :param data: 包含 'name' 與 'type' 的字典
        """
        try:
            with get_db() as db:
                cursor = db.execute(
                    'INSERT INTO categories (name, type, is_default) VALUES (?, ?, 0)',
                    (data.get('name'), data.get('type'))
                )
                db.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error in Category.create: {e}")
            return None

    @classmethod
    def update(cls, cat_id: int, data: dict):
        """
        更新分類
        :param cat_id: 分類 ID
        :param data: 包含 'name' 與 'type' 的字典
        """
        try:
            with get_db() as db:
                # 只允許更新非預設的分類
                cursor = db.execute('SELECT is_default FROM categories WHERE id = ?', (cat_id,))
                row = cursor.fetchone()
                if not row or row['is_default']:
                    return False
                
                db.execute('UPDATE categories SET name = ?, type = ? WHERE id = ?', 
                           (data.get('name'), data.get('type'), cat_id))
                db.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error in Category.update: {e}")
            return False

    @classmethod
    def delete(cls, cat_id: int):
        """
        刪除指定分類（預設分類不可刪除）
        :param cat_id: 分類 ID
        """
        try:
            with get_db() as db:
                cursor = db.execute('SELECT is_default FROM categories WHERE id = ?', (cat_id,))
                row = cursor.fetchone()
                if not row or row['is_default']:
                    return False
                db.execute('DELETE FROM categories WHERE id = ?', (cat_id,))
                db.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error in Category.delete: {e}")
            return False
