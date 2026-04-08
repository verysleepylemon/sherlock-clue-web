# 🕸️ 线索网 (Clue Web) — OSINT Investigation Platform

<p align="center">
  <img src="assets/banner.png" alt="线索网 Banner" width="100%">
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/sherlock-project/sherlock"><img src="https://img.shields.io/badge/sherlock-v0.16.0_patched-brightgreen" alt="Sherlock v0.16.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
</p>
<p align="center">
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>線索網</strong><br>
  <em>一個視覺化 OSINT 調查工具，將數位足跡映射到 400+ 平台上，<br>產生互動式蛛網情報看板。</em>
</p>

<p align="center">
  <strong>🌐 其他語言版本：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>---

## 展示

### 終端輸出

<p align="center">
  <img src="assets/demo_terminal.gif" alt="終端展示 — 執行 investigate.py" width="780">
</p>

### 線索網調查看板

<p align="center">
  <img src="assets/clue_web_ui.png" alt="線索網 UI — 互動式調查看板" width="100%">
</p>

<p align="center"><em>互動式蛛網圖，支援縮放、平移、深度著色、上下文面板、小地圖等 — 靈感來自 <a href="https://gitnexus.dev">GitNexus</a></em></p>

---

## 什麼是線索網？

這是 [Sherlock](https://github.com/sherlock-project/sherlock) 的**增強分叉版本** — 著名的使用者名稱 OSINT（開源情報）工具。在原版 Sherlock 基礎上，本分叉增加了：

1. **9個Bug修復** — 透過 [GitNexus](https://gitnexus.dev) 程式碼智慧引擎逆向工程原始程式碼庫發現（2個嚴重、5個中等、1個Bug、1個次要）
2. **線索網 (Clue Web)** — 全功能調查視覺化工具，產生互動式 HTML 調查看板，靈感來自 GitNexus 的蛛網圖介面

---

## GitNexus 和 Sherlock 如何協同運作

| 元件 | 作用 |
|------|------|
| **GitNexus** | 程式碼智慧引擎 — 逆向工程 Sherlock 的呼叫圖、追蹤執行流程，在3個檔案中識別出9個Bug。其蛛網視覺化設計啟發了線索網的 UI。 |
| **Sherlock**（已修補）| 核心使用者名稱列舉引擎 — 檢查400+平台。本分叉包含所有9個Bug修復。 |
| **線索網** | 調查視覺化層 — 將 Sherlock 的輸出渲染為互動式節點圖，支援縮放、平移、篩選、深度著色和上下文面板。 |

---

## 快速開始

```bash
# 複製本分叉
git clone https://github.com/verysleepylemon/sherlock.git
cd sherlock

# 建立虛擬環境
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 安裝依賴
pip install -e .

# 執行調查
python investigate.py <使用者名稱>

# 範例
python investigate.py john_doe
python investigate.py sleepy_lemonade --timeout 20
python investigate.py "my username" --max-variations 6 --no-browser
```

HTML 調查看板會自動在瀏覽器中開啟。

---

## 線索網功能（GitNexus 風格）

| 功能 | 說明 |
|------|------|
| **縮放和平移** | 滑鼠滾輪縮放，右鍵拖動平移 |
| **節點拖曳** | 左鍵拖動任意節點重新定位 |
| **深度影響著色** | 從選中節點 BFS：d=1 明亮 → d=2 中等 → d=3+ 暗淡（類似 GitNexus 影響範圍） |
| **上下文面板** | 點擊任意節點 → 右側面板顯示360°檢視（目標/變體/分類/站點） |
| **變體篩選** | 點擊使用者名稱變體 → 僅顯示該變體找到的平台 |
| **分類開關** | 顯示/隱藏整個分類（社交、遊戲、科技、創意、金融、論壇、學術、其他） |
| **即時搜尋** | 在搜尋列輸入，非匹配節點變暗 |
| **小地圖** | 右下角小地圖，點擊傳送 |
| **麵包屑導覽** | 底欄可點擊路徑：目標 → 變體 → 分類 → 站點 |
| **匯出** | 一鍵複製所有已發現的 URL |
| **快速鍵** | `R` = 配合檢視, `Esc` = 取消選擇, `+/-` = 縮放, 雙擊 = 重置 |
| **檢視模式** | 蛛網（預設）/ 放射 / 聚焦 |
| **動畫邊線** | 高亮連接上的粒子動畫 |

---

## 已修復的Bug（共9個）

| # | 嚴重性 | 檔案 | 描述 |
|---|--------|------|------|
| 1 | **嚴重** | `sherlock.py` | `errorType` 列表/字串不一致 — 列表類型的 `errorType` 靜默使用了錯誤的HTTP方法（+29個額外平台被偵測到） |
| 2 | **嚴重** | `sherlock.py` | `response_text = r.text.encode()` 導致所有下游比較中的 bytes/str 不匹配 |
| 3 | **Bug** | `notify.py` | `finish()` 中的偏移錯誤 |
| 4 | **中等** | `notify.py` | 執行緒不安全的全域計數器 |
| 5 | **中等** | `sites.py` | 可變預設引數 |
| 6 | **中等** | `sites.py` | `username_unclaimed` 總是被隨機令牌覆蓋 |
| 7 | **中等** | `sherlock.py` | `--no-print-found` argparse 邏輯反轉 |
| 8 | **中等** | `sherlock.py` | WAF 偵測在回應為 `None` 時當機 |
| 9 | **次要** | `sherlock.py` | 版本前綴剝離過於激進 |

---

## 使用者名稱變體引擎

工具自動產生目標使用者名稱的替代形式：

| 輸入 | 產生的變體 |
|------|-----------|
| `sleepy_lemonade` | `sleepy_lemonade`, `sleepylemonade`, `sleepy.lemonade`, `sleepy-lemonade`, `sleepyLemonade`, `SleepyLemonade`, `lemonade_sleepy`, `lemonadesleepy` |

每個變體在 400+ 平台上搜尋，結果去重後在線索網中視覺化顯示。

---

## CLI 選項

| 參數 | 預設值 | 描述 |
|------|--------|------|
| `username` | （必填）| 要調查的目標使用者名稱 |
| `--timeout` | `10` | 每個站點的逾時時間（秒） |
| `--max-variations` | `8` | 最大使用者名稱變體數 |
| `--no-browser` | `false` | 不自動開啟 HTML 結果 |

---

## 專案結構

```
sherlock/
├── investigate.py              # 線索網調查執行器
├── clue_web_template.html      # GitNexus 風格視覺化模板
├── assets/
│   ├── banner.png              # 儲存庫橫幅
│   ├── demo_terminal.gif       # 終端輸出展示
│   └── clue_web_ui.png         # UI 截圖
├── sherlock_project/
│   ├── sherlock.py             # 核心引擎（修復5個Bug）
│   ├── notify.py               # 結果通知（修復2個Bug）
│   ├── sites.py                # 站點定義（修復2個Bug）
│   └── resources/
│       └── data.json           # 400+ 平台定義
├── wiki/                       # 詳細文件
├── README.md                   # English
├── README.zh-CN.md             # 简体中文
├── README.zh-TW.md             # 繁體中文（本檔案）
├── README.ja.md                # 日本語
└── README.ms.md                # Bahasa Melayu
```

---

## 文件

| 頁面 | 描述 |
|------|------|
| [架構](wiki/Architecture.md) | 系統架構、節點類型、資料流 |
| [Bug修復詳情](wiki/Bug-Fixes-Detailed.md) | 所有9個Bug的深入分析 |
| [線索網UI指南](wiki/Clue-Web-UI-Guide.md) | 調查看板完整指南 |
| [使用者名稱變體引擎](wiki/Username-Variation-Engine.md) | 變體產生方式 |
| [GitNexus整合](wiki/GitNexus-Integration.md) | GitNexus 的使用方式 |
| [常見問題](wiki/FAQ.md) | 常見問題解答 |

---

## 致謝

- **[Sherlock Project](https://github.com/sherlock-project/sherlock)** — 原始 OSINT 使用者名稱列舉工具
- **[GitNexus](https://gitnexus.dev)** — 程式碼智慧引擎：呼叫圖分析發現了9個Bug，蛛網視覺化啟發了線索網 UI
- **線索網 (Clue Web)** — GitNexus + Sherlock 協同建構

## 授權條款

本專案是 [Sherlock](https://github.com/sherlock-project/sherlock) 的分叉，採用 [MIT 授權條款](LICENSE)。
