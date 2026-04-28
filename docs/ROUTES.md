# 路由設計文件 (API & Route Design)

本文件依據 PRD 與架構文件，定義系統的所有 Flask 路由、HTTP 方法及對應的 Jinja2 模板。

## 1. 路由總覽表格

| 功能模組 | 動作描述 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **Dashboard** | 儀表板首頁 | `GET` | `/` | `dashboard/index.html` | 顯示當前月份收支概況與近期明細 |
| **Transactions** | 新增收支頁面 | `GET` | `/transactions/new` | `transactions/form.html` | 顯示新增表單 |
| **Transactions** | 建立收支紀錄 | `POST` | `/transactions/new` | — | 接收表單並寫入資料庫，成功後重導向至首頁 |
| **Transactions** | 編輯收支頁面 | `GET` | `/transactions/<id>/edit`| `transactions/form.html` | 顯示帶有原始資料的編輯表單 |
| **Transactions** | 更新收支紀錄 | `POST` | `/transactions/<id>/edit`| — | 接收表單並更新資料庫，成功後重導向至首頁 |
| **Transactions** | 刪除收支紀錄 | `POST` | `/transactions/<id>/delete`| — | 刪除指定紀錄，成功後重導向至首頁 |
| **Reports** | 檢視歷史報表 | `GET` | `/reports` | `reports/index.html` | 顯示歷史月份報表與圖表資料 |
| **Settings** | 系統設定頁面 | `GET` | `/settings` | `settings/index.html` | 顯示全域設定與自訂分類清單 |
| **Settings** | 更新全域設定 | `POST` | `/settings/update` | — | 更新起始日等設定，成功後重導向至設定頁 |
| **Settings** | 新增自訂分類 | `POST` | `/settings/categories` | — | 建立新的收支分類，成功後重導向至設定頁 |
| **Settings** | 刪除自訂分類 | `POST` | `/settings/categories/<id>/delete`| — | 刪除指定的分類，成功後重導向至設定頁 |

## 2. 詳細路由說明

### Dashboard
* `GET /`:
  * **輸入**: 無。
  * **邏輯**: 透過 Service 計算當月自訂起訖日，查詢該區間的明細與總結。
  * **輸出**: 渲染 `dashboard/index.html`。

### Transactions
* `GET /transactions/new`:
  * **輸出**: 取得所有可用分類，渲染 `transactions/form.html`。
* `POST /transactions/new`:
  * **輸入**: 表單資料 (`amount`, `type`, `category_id`, `date`, `note`)
  * **邏輯**: 驗證資料後呼叫 `Transaction.create`。
  * **輸出**: 成功則重導向 `/`，失敗則返回 400 或重新渲染表單。
* `POST /transactions/<id>/delete`:
  * **輸入**: URL 中的 `id`。
  * **邏輯**: 呼叫 `Transaction.delete`。
  * **輸出**: 重導向至 `/`。

### Reports
* `GET /reports`:
  * **輸入**: `month` 參數 (選填)。
  * **邏輯**: 依照月份查詢歷史總結，整理給 Chart.js 用的資料。
  * **輸出**: 渲染 `reports/index.html`。

### Settings
* `GET /settings`:
  * **邏輯**: 取得目前的設定值 (`month_start_day`) 與所有分類。
  * **輸出**: 渲染 `settings/index.html`。
* `POST /settings/update`:
  * **輸入**: 表單資料 (`month_start_day`)
  * **邏輯**: 更新設定，確保數字在 1~28 之間。

## 3. Jinja2 模板清單

所有的 HTML 檔案皆存放於 `templates/` 目錄，規劃如下：
* `base.html`: 共用母版 (包含 Navbar, Header, 載入共用 CSS/JS)。
* `dashboard/index.html`: 儀表板頁面，繼承 `base.html`。
* `transactions/form.html`: 共用的新增與編輯表單頁面，繼承 `base.html`。
* `reports/index.html`: 報表與圖表頁面，繼承 `base.html`。
* `settings/index.html`: 設定管理頁面，繼承 `base.html`。
