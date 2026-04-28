-- 建立 categories 資料表
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    is_default BOOLEAN NOT NULL DEFAULT 0
);

-- 建立 transactions 資料表
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);

-- 建立 settings 資料表
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL
);

-- 寫入系統預設設定
INSERT OR IGNORE INTO settings (key, value) VALUES ('month_start_day', '1');

-- 寫入預設收支分類
INSERT OR IGNORE INTO categories (id, name, type, is_default) VALUES 
(1, '薪水', 'income', 1),
(2, '投資', 'income', 1),
(3, '餐飲', 'expense', 1),
(4, '交通', 'expense', 1),
(5, '娛樂', 'expense', 1),
(6, '居家', 'expense', 1);
