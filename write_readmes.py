"""Generate separate README files per language with embedded visuals."""
from pathlib import Path

DIR = Path(__file__).parent

LANG_SWITCHER_EN = """\
<p align="center">
  <strong>🌐 README in other languages:</strong><br>
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.zh-TW.md">🇹🇼 繁體中文</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>"""

LANG_SWITCHER_ZH_CN = """\
<p align="center">
  <strong>🌐 其他语言版本：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-TW.md">🇹🇼 繁體中文</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>"""

LANG_SWITCHER_ZH_TW = """\
<p align="center">
  <strong>🌐 其他語言版本：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>"""

LANG_SWITCHER_JA = """\
<p align="center">
  <strong>🌐 他の言語版：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.zh-TW.md">🇹🇼 繁體中文</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>"""

LANG_SWITCHER_MS = """\
<p align="center">
  <strong>🌐 Versi bahasa lain：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.zh-TW.md">🇹🇼 繁體中文</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a>
</p>"""

# ─── Shared header block (banner + badges) ───
HEADER = """\
# 🕸️ 线索网 (Clue Web) — OSINT Investigation Platform

<p align="center">
  <img src="assets/banner.png" alt="线索网 Banner" width="100%">
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/sherlock-project/sherlock"><img src="https://img.shields.io/badge/sherlock-v0.16.0_patched-brightgreen" alt="Sherlock v0.16.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
</p>
"""

DEMO_SECTION_EN = """\
---

## Demo

### Terminal Output

<p align="center">
  <img src="assets/demo_terminal.gif" alt="Terminal demo — running investigate.py" width="780">
</p>

### Clue Web Investigation Board

<p align="center">
  <img src="assets/clue_web_ui.png" alt="Clue Web UI — interactive investigation board" width="100%">
</p>

<p align="center"><em>Interactive spider-web graph with zoom, pan, depth coloring, context panels, minimap, and more — inspired by <a href="https://gitnexus.dev">GitNexus</a></em></p>
"""

DEMO_SECTION_ZH = """\
---

## 演示

### 终端输出

<p align="center">
  <img src="assets/demo_terminal.gif" alt="终端演示 — 运行 investigate.py" width="780">
</p>

### 线索网调查看板

<p align="center">
  <img src="assets/clue_web_ui.png" alt="线索网 UI — 交互式调查看板" width="100%">
</p>

<p align="center"><em>交互式蛛网图，支持缩放、平移、深度着色、上下文面板、小地图等 — 灵感来自 <a href="https://gitnexus.dev">GitNexus</a></em></p>
"""

DEMO_SECTION_ZH_TW = """\
---

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
"""

DEMO_SECTION_JA = """\
---

## デモ

### ターミナル出力

<p align="center">
  <img src="assets/demo_terminal.gif" alt="ターミナルデモ — investigate.py の実行" width="780">
</p>

### 线索网 調査ボード

<p align="center">
  <img src="assets/clue_web_ui.png" alt="Clue Web UI — インタラクティブ調査ボード" width="100%">
</p>

<p align="center"><em>インタラクティブなスパイダーウェブグラフ：ズーム、パン、深度カラーリング、コンテキストパネル、ミニマップなど — <a href="https://gitnexus.dev">GitNexus</a> にインスパイア</em></p>
"""

DEMO_SECTION_MS = """\
---

## Demo

### Output Terminal

<p align="center">
  <img src="assets/demo_terminal.gif" alt="Demo terminal — menjalankan investigate.py" width="780">
</p>

### Papan Siasatan 线索网

<p align="center">
  <img src="assets/clue_web_ui.png" alt="UI Clue Web — papan siasatan interaktif" width="100%">
</p>

<p align="center"><em>Graf web labah-labah interaktif dengan zum, seret, pewarnaan kedalaman, panel konteks, peta mini dan lain-lain — diilhamkan oleh <a href="https://gitnexus.dev">GitNexus</a></em></p>
"""

# ─── ENGLISH ────────────────────────────────────────────────────────

README_EN = HEADER + """\
<p align="center">
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>线索网</strong><br>
  <em>A visual OSINT investigation tool that maps digital footprints across 400+ platforms<br>into an interactive spider-web intelligence board.</em>
</p>

""" + LANG_SWITCHER_EN + DEMO_SECTION_EN + """
---

## What Is This?

This is a **forked and enhanced** version of [Sherlock](https://github.com/sherlock-project/sherlock) — the well-known username OSINT tool. On top of the original Sherlock, this fork adds:

1. **9 Bug Fixes** — identified by reverse-engineering the codebase with [GitNexus](https://gitnexus.dev) code intelligence (2 critical, 5 medium, 1 bug, 1 minor)
2. **线索网 (Clue Web)** — a full-featured investigation visualization that generates interactive HTML boards, inspired by GitNexus's spider-web graph

---

## How GitNexus and Sherlock Work Together

| Component | Role |
|-----------|------|
| **GitNexus** | Code intelligence engine — reverse-engineered Sherlock's call graph, traced execution flows, identified 9 bugs across 3 files. Its spider-web visualization inspired the Clue Web UI. |
| **Sherlock** (patched) | Core username enumeration engine — checks 400+ platforms. This fork includes all 9 bug fixes. |
| **线索网 (Clue Web)** | Investigation visualization layer — renders Sherlock's output as an interactive node graph with zoom, pan, filtering, depth coloring, and context panels. |

---

## Quick Start

```bash
# Clone this fork
git clone https://github.com/verysleepylemon/sherlock.git
cd sherlock

# Create virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -e .

# Run investigation
python investigate.py <username>

# Examples
python investigate.py john_doe
python investigate.py sleepy_lemonade --timeout 20
python investigate.py "my username" --max-variations 6 --no-browser
```

The HTML investigation board opens automatically in your browser.

---

## Clue Web Features (GitNexus-Inspired)

| Feature | Description |
|---------|-------------|
| **Zoom & Pan** | Mouse wheel to zoom, right-click drag to pan |
| **Node Drag** | Left-click drag any node to reposition |
| **Depth Impact Coloring** | BFS from selected node: d=1 bright → d=2 medium → d=3+ dim (like GitNexus blast radius) |
| **Context Panel** | Click any node → right panel shows 360° view per type (TARGET / VARIANT / CATEGORY / SITE) |
| **Variant Filter** | Click a username variant → isolates only that variant's found platforms |
| **Category Toggles** | Show/hide categories (Social, Gaming, Tech, Creative, Finance, Forums, Academic, Other) |
| **Real-Time Search** | Type to dim non-matching nodes |
| **Minimap** | Bottom-right minimap with viewport rectangle — click to teleport |
| **Breadcrumb** | Clickable navigation: Target → Variant → Category → Site |
| **Export** | One-click copy all URLs to clipboard |
| **Keyboard Shortcuts** | `R` = fit view, `Esc` = deselect, `+/-` = zoom, double-click = reset |
| **View Modes** | Web (default) / Radial / Focus layouts |
| **Animated Edges** | Particle animation on highlighted connections |

---

## Bug Fixes Applied (9 Total)

| # | Severity | File | Description |
|---|----------|------|-------------|
| 1 | **CRITICAL** | `sherlock.py` | `errorType` list/string inconsistency — sites with list `errorType` silently used wrong HTTP method (+29 extra platforms detected) |
| 2 | **CRITICAL** | `sherlock.py` | `response_text = r.text.encode()` caused bytes/str mismatch in all downstream comparisons |
| 3 | **BUG** | `notify.py` | Off-by-one in `finish()` — `countResults()-1` instead of `getResults()` |
| 4 | **MEDIUM** | `notify.py` | Thread-unsafe global counter. Replaced with `threading.Lock()` |
| 5 | **MEDIUM** | `sites.py` | Mutable default argument `do_not_exclude=[]` |
| 6 | **MEDIUM** | `sites.py` | `username_unclaimed` always overwritten by random token |
| 7 | **MEDIUM** | `sherlock.py` | `--no-print-found` argparse logic inverted |
| 8 | **MEDIUM** | `sherlock.py` | WAF detection crashed on `None` response |
| 9 | **MINOR** | `sherlock.py` | Version strip `.lstrip("v")` too aggressive |

---

## Username Variation Engine

The tool automatically generates alternate forms of the target username:

| Input | Variations Generated |
|-------|---------------------|
| `sleepy_lemonade` | `sleepy_lemonade`, `sleepylemonade`, `sleepy.lemonade`, `sleepy-lemonade`, `sleepyLemonade`, `SleepyLemonade`, `lemonade_sleepy`, `lemonadesleepy` |

Each variation is searched across 400+ platforms, results are deduplicated, and combined findings are visualized in the Clue Web.

---

## CLI Options

| Flag | Default | Description |
|------|---------|-------------|
| `username` | (required) | Target username to investigate |
| `--timeout` | `10` | Timeout per site in seconds |
| `--max-variations` | `8` | Maximum username variations to generate |
| `--no-browser` | `false` | Don't auto-open the HTML result |

---

## Project Structure

```
sherlock/
├── investigate.py              # 线索网 investigation runner
├── clue_web_template.html      # GitNexus-style visualization template
├── assets/
│   ├── banner.png              # Repository banner
│   ├── demo_terminal.gif       # Terminal output demo
│   └── clue_web_ui.png         # UI mockup screenshot
├── sherlock_project/
│   ├── sherlock.py             # Core engine (5 bugs fixed)
│   ├── notify.py               # Result notification (2 bugs fixed)
│   ├── sites.py                # Site definitions (2 bugs fixed)
│   └── resources/
│       └── data.json           # 400+ platform definitions
├── wiki/                       # Detailed documentation
├── README.md                   # English (this file)
├── README.zh-CN.md             # 简体中文
├── README.zh-TW.md             # 繁體中文
├── README.ja.md                # 日本語
└── README.ms.md                # Bahasa Melayu
```

---

## Documentation

| Page | Description |
|------|-------------|
| [Architecture](wiki/Architecture.md) | System architecture, node types, data flow |
| [Bug Fixes Detailed](wiki/Bug-Fixes-Detailed.md) | Deep dive into all 9 bugs |
| [Clue Web UI Guide](wiki/Clue-Web-UI-Guide.md) | Full guide to the investigation board |
| [Username Variation Engine](wiki/Username-Variation-Engine.md) | How variations work |
| [GitNexus Integration](wiki/GitNexus-Integration.md) | How GitNexus was used |
| [FAQ](wiki/FAQ.md) | Frequently Asked Questions |

---

## Credits

- **[Sherlock Project](https://github.com/sherlock-project/sherlock)** — Original OSINT username enumeration tool
- **[GitNexus](https://gitnexus.dev)** — Code intelligence engine: call graph analysis found the 9 bugs, spider-web visualization inspired the Clue Web UI
- **线索网 (Clue Web)** — Built with GitNexus + Sherlock synergy

## License

This project is a fork of [Sherlock](https://github.com/sherlock-project/sherlock), licensed under the [MIT License](LICENSE).
"""

# ─── SIMPLIFIED CHINESE ─────────────────────────────────────────────

README_ZH_CN = HEADER + """\
<p align="center">
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>线索网</strong><br>
  <em>一个可视化 OSINT 调查工具，将数字足迹映射到 400+ 平台上，<br>生成交互式蛛网情报看板。</em>
</p>

""" + LANG_SWITCHER_ZH_CN + DEMO_SECTION_ZH + """
---

## 什么是线索网？

这是 [Sherlock](https://github.com/sherlock-project/sherlock) 的**增强分叉版本** — 著名的用户名 OSINT（开源情报）工具。在原版 Sherlock 基础上，本分叉增加了：

1. **9个Bug修复** — 通过 [GitNexus](https://gitnexus.dev) 代码智能引擎逆向工程原始代码库发现（2个严重、5个中等、1个Bug、1个次要）
2. **线索网 (Clue Web)** — 全功能调查可视化工具，生成交互式 HTML 调查看板，灵感来自 GitNexus 的蛛网图界面

---

## GitNexus 和 Sherlock 如何协同工作

| 组件 | 作用 |
|------|------|
| **GitNexus** | 代码智能引擎 — 逆向工程 Sherlock 的调用图、跟踪执行流程，在3个文件中识别出9个Bug。其蛛网可视化设计启发了线索网的 UI。 |
| **Sherlock**（已修补）| 核心用户名枚举引擎 — 检查400+平台。本分叉包含所有9个Bug修复。 |
| **线索网** | 调查可视化层 — 将 Sherlock 的输出渲染为交互式节点图，支持缩放、平移、筛选、深度着色和上下文面板。 |

---

## 快速开始

```bash
# 克隆本分叉
git clone https://github.com/verysleepylemon/sherlock.git
cd sherlock

# 创建虚拟环境
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate

# 安装依赖
pip install -e .

# 运行调查
python investigate.py <用户名>

# 示例
python investigate.py john_doe
python investigate.py sleepy_lemonade --timeout 20
python investigate.py "my username" --max-variations 6 --no-browser
```

HTML 调查看板会自动在浏览器中打开。

---

## 线索网功能（GitNexus 风格）

| 功能 | 说明 |
|------|------|
| **缩放和平移** | 鼠标滚轮缩放，右键拖动平移 |
| **节点拖拽** | 左键拖动任意节点重新定位 |
| **深度影响着色** | 从选中节点 BFS：d=1 明亮 → d=2 中等 → d=3+ 暗淡（类似 GitNexus 影响范围） |
| **上下文面板** | 点击任意节点 → 右侧面板显示360°视图（目标/变体/分类/站点） |
| **变体筛选** | 点击用户名变体 → 仅显示该变体找到的平台 |
| **分类开关** | 显示/隐藏整个分类（社交、游戏、科技、创意、金融、论坛、学术、其他） |
| **实时搜索** | 在搜索栏输入，非匹配节点变暗 |
| **小地图** | 右下角小地图，点击传送 |
| **面包屑导航** | 底栏可点击路径：目标 → 变体 → 分类 → 站点 |
| **导出** | 一键复制所有已发现的 URL |
| **快捷键** | `R` = 适应视图, `Esc` = 取消选择, `+/-` = 缩放, 双击 = 重置 |
| **视图模式** | 蛛网（默认）/ 放射 / 聚焦 |
| **动画边线** | 高亮连接上的粒子动画 |

---

## 已修复的Bug（共9个）

| # | 严重性 | 文件 | 描述 |
|---|--------|------|------|
| 1 | **严重** | `sherlock.py` | `errorType` 列表/字符串不一致 — 列表类型的 `errorType` 静默使用了错误的HTTP方法（+29个额外平台被检测到） |
| 2 | **严重** | `sherlock.py` | `response_text = r.text.encode()` 导致所有下游比较中的 bytes/str 不匹配 |
| 3 | **Bug** | `notify.py` | `finish()` 中的偏移错误 — `countResults()-1` 而非 `getResults()` |
| 4 | **中等** | `notify.py` | 线程不安全的全局计数器。替换为 `threading.Lock()` |
| 5 | **中等** | `sites.py` | 可变默认参数 `do_not_exclude=[]` |
| 6 | **中等** | `sites.py` | `username_unclaimed` 总是被随机令牌覆盖 |
| 7 | **中等** | `sherlock.py` | `--no-print-found` argparse 逻辑反转 |
| 8 | **中等** | `sherlock.py` | WAF 检测在响应为 `None` 时崩溃 |
| 9 | **次要** | `sherlock.py` | 版本前缀剥离 `.lstrip("v")` 过于激进 |

---

## 用户名变体引擎

工具自动生成目标用户名的替代形式：

| 输入 | 生成的变体 |
|------|-----------|
| `sleepy_lemonade` | `sleepy_lemonade`, `sleepylemonade`, `sleepy.lemonade`, `sleepy-lemonade`, `sleepyLemonade`, `SleepyLemonade`, `lemonade_sleepy`, `lemonadesleepy` |

每个变体在 400+ 平台上搜索，结果去重后在线索网中可视化显示。

---

## CLI 选项

| 参数 | 默认值 | 描述 |
|------|--------|------|
| `username` | （必填）| 要调查的目标用户名 |
| `--timeout` | `10` | 每个站点的超时时间（秒） |
| `--max-variations` | `8` | 最大用户名变体数 |
| `--no-browser` | `false` | 不自动打开 HTML 结果 |

---

## 项目结构

```
sherlock/
├── investigate.py              # 线索网调查运行器
├── clue_web_template.html      # GitNexus 风格可视化模板
├── assets/
│   ├── banner.png              # 仓库横幅
│   ├── demo_terminal.gif       # 终端输出演示
│   └── clue_web_ui.png         # UI 截图
├── sherlock_project/
│   ├── sherlock.py             # 核心引擎（修复5个Bug）
│   ├── notify.py               # 结果通知（修复2个Bug）
│   ├── sites.py                # 站点定义（修复2个Bug）
│   └── resources/
│       └── data.json           # 400+ 平台定义
├── wiki/                       # 详细文档
├── README.md                   # English
├── README.zh-CN.md             # 简体中文（本文件）
├── README.zh-TW.md             # 繁體中文
├── README.ja.md                # 日本語
└── README.ms.md                # Bahasa Melayu
```

---

## 文档

| 页面 | 描述 |
|------|------|
| [架构](wiki/Architecture.md) | 系统架构、节点类型、数据流 |
| [Bug修复详情](wiki/Bug-Fixes-Detailed.md) | 所有9个Bug的深入分析 |
| [线索网UI指南](wiki/Clue-Web-UI-Guide.md) | 调查看板完整指南 |
| [用户名变体引擎](wiki/Username-Variation-Engine.md) | 变体生成方式 |
| [GitNexus集成](wiki/GitNexus-Integration.md) | GitNexus 的使用方式 |
| [常见问题](wiki/FAQ.md) | 常见问题解答 |

---

## 致谢

- **[Sherlock Project](https://github.com/sherlock-project/sherlock)** — 原始 OSINT 用户名枚举工具
- **[GitNexus](https://gitnexus.dev)** — 代码智能引擎：调用图分析发现了9个Bug，蛛网可视化启发了线索网 UI
- **线索网 (Clue Web)** — GitNexus + Sherlock 协同构建

## 许可证

本项目是 [Sherlock](https://github.com/sherlock-project/sherlock) 的分叉，采用 [MIT 许可证](LICENSE)。
"""

# ─── TRADITIONAL CHINESE ─────────────────────────────────────────────

README_ZH_TW = HEADER + """\
<p align="center">
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>線索網</strong><br>
  <em>一個視覺化 OSINT 調查工具，將數位足跡映射到 400+ 平台上，<br>產生互動式蛛網情報看板。</em>
</p>

""" + LANG_SWITCHER_ZH_TW + DEMO_SECTION_ZH_TW + """
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
.venv\\Scripts\\activate
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
"""

# ─── JAPANESE ────────────────────────────────────────────────────────

README_JA = HEADER + """\
<p align="center">
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>线索网</strong><br>
  <em>400以上のプラットフォームにわたるデジタルフットプリントを<br>インタラクティブなスパイダーウェブ情報ボードに可視化するOSINT調査ツール。</em>
</p>

""" + LANG_SWITCHER_JA + DEMO_SECTION_JA + """
---

## 线索网（手がかりウェブ）とは？

これは [Sherlock](https://github.com/sherlock-project/sherlock) の**拡張フォーク版**です — 有名なユーザー名 OSINT（オープンソースインテリジェンス）ツール。オリジナルの Sherlock に加えて、このフォークは以下を追加：

1. **9つのバグ修正** — [GitNexus](https://gitnexus.dev) コードインテリジェンスエンジンでコードベースをリバースエンジニアリングして発見（重大2、中程度5、バグ1、軽微1）
2. **线索网（Clue Web）** — フル機能の調査可視化ツール。インタラクティブな HTML 調査ボードを生成。GitNexus のスパイダーウェブグラフにインスパイア。

---

## GitNexus と Sherlock の連携

| コンポーネント | 役割 |
|----------------|------|
| **GitNexus** | コードインテリジェンスエンジン — Sherlock のコールグラフをリバースエンジニアリングし、実行フローを追跡し、3つのファイルで9つのバグを特定。スパイダーウェブ可視化が Clue Web の UI にインスピレーション。 |
| **Sherlock**（パッチ済み）| コアのユーザー名列挙エンジン — 400以上のプラットフォームを検査。このフォークには全9つのバグ修正を含む。 |
| **线索网** | 調査可視化レイヤー — Sherlock の出力をインタラクティブなノードグラフとしてレンダリング。ズーム、パン、フィルタリング、深度カラーリング、コンテキストパネル搭載。 |

---

## クイックスタート

```bash
# このフォークをクローン
git clone https://github.com/verysleepylemon/sherlock.git
cd sherlock

# 仮想環境を作成
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate

# 依存関係をインストール
pip install -e .

# 調査を実行
python investigate.py <ユーザー名>

# 例
python investigate.py john_doe
python investigate.py sleepy_lemonade --timeout 20
python investigate.py "my username" --max-variations 6 --no-browser
```

HTML 調査ボードが自動的にブラウザで開きます。

---

## 线索网の機能（GitNexus スタイル）

| 機能 | 説明 |
|------|------|
| **ズームとパン** | マウスホイールでズーム、右クリックドラッグでパン |
| **ノードドラッグ** | 左クリックドラッグで任意のノードを再配置 |
| **深度影響カラーリング** | 選択ノードから BFS：d=1 明るい → d=2 中程度 → d=3+ 暗い（GitNexus 影響範囲に類似） |
| **コンテキストパネル** | 任意のノードをクリック → 右パネルに360°ビューを表示（ターゲット/バリアント/カテゴリ/サイト） |
| **バリアントフィルター** | ユーザー名バリアントをクリック → そのバリアントのプラットフォームのみ表示 |
| **カテゴリトグル** | カテゴリ全体の表示/非表示（ソーシャル、ゲーム、テック、クリエイティブ、金融、フォーラム、学術、その他） |
| **リアルタイム検索** | 検索バーに入力して非一致ノードを暗くする |
| **ミニマップ** | 右下のミニマップ、クリックでテレポート |
| **パンくずナビ** | 下部バーにクリック可能なパス：ターゲット → バリアント → カテゴリ → サイト |
| **エクスポート** | ワンクリックですべての URL をクリップボードにコピー |
| **キーボードショートカット** | `R` = フィット, `Esc` = 選択解除, `+/-` = ズーム, ダブルクリック = リセット |
| **ビューモード** | ウェブ（デフォルト）/ ラジアル / フォーカス |
| **アニメーションエッジ** | ハイライト接続にパーティクルアニメーション |

---

## 修正されたバグ（合計9つ）

| # | 重大度 | ファイル | 説明 |
|---|--------|---------|------|
| 1 | **重大** | `sherlock.py` | `errorType` のリスト/文字列不整合 — リスト型 `errorType` がHTTPメソッドを誤使用（+29プラットフォーム検出） |
| 2 | **重大** | `sherlock.py` | `response_text = r.text.encode()` が全下流比較で bytes/str 不一致を引き起こす |
| 3 | **バグ** | `notify.py` | `finish()` のオフバイワン |
| 4 | **中程度** | `notify.py` | スレッドアンセーフなグローバルカウンター |
| 5 | **中程度** | `sites.py` | ミュータブルデフォルト引数 |
| 6 | **中程度** | `sites.py` | `username_unclaimed` が常にランダムトークンで上書き |
| 7 | **中程度** | `sherlock.py` | `--no-print-found` argparse ロジック反転 |
| 8 | **中程度** | `sherlock.py` | WAF 検出がレスポンス `None` でクラッシュ |
| 9 | **軽微** | `sherlock.py` | バージョンプレフィックス除去が過剰 |

---

## ユーザー名バリエーションエンジン

ツールはターゲットユーザー名の代替形式を自動生成：

| 入力 | 生成されるバリエーション |
|------|----------------------|
| `sleepy_lemonade` | `sleepy_lemonade`, `sleepylemonade`, `sleepy.lemonade`, `sleepy-lemonade`, `sleepyLemonade`, `SleepyLemonade`, `lemonade_sleepy`, `lemonadesleepy` |

各バリエーションは 400+ プラットフォームで検索され、結果は重複排除後、线索网で可視化。

---

## CLI オプション

| フラグ | デフォルト | 説明 |
|--------|-----------|------|
| `username` | （必須）| 調査対象のユーザー名 |
| `--timeout` | `10` | サイトあたりのタイムアウト（秒） |
| `--max-variations` | `8` | 最大バリエーション数 |
| `--no-browser` | `false` | HTML 結果を自動オープンしない |

---

## プロジェクト構造

```
sherlock/
├── investigate.py              # 线索网調査ランナー
├── clue_web_template.html      # GitNexus スタイル可視化テンプレート
├── assets/
│   ├── banner.png              # リポジトリバナー
│   ├── demo_terminal.gif       # ターミナル出力デモ
│   └── clue_web_ui.png         # UI スクリーンショット
├── sherlock_project/
│   ├── sherlock.py             # コアエンジン（5バグ修正）
│   ├── notify.py               # 結果通知（2バグ修正）
│   ├── sites.py                # サイト定義（2バグ修正）
│   └── resources/
│       └── data.json           # 400+ プラットフォーム定義
├── wiki/                       # 詳細ドキュメント
├── README.md                   # English
├── README.zh-CN.md             # 简体中文
├── README.zh-TW.md             # 繁體中文
├── README.ja.md                # 日本語（このファイル）
└── README.ms.md                # Bahasa Melayu
```

---

## ドキュメント

| ページ | 説明 |
|--------|------|
| [アーキテクチャ](wiki/Architecture.md) | システム構成、ノードタイプ、データフロー |
| [バグ修正詳細](wiki/Bug-Fixes-Detailed.md) | 全9バグの詳細分析 |
| [Clue Web UIガイド](wiki/Clue-Web-UI-Guide.md) | 調査ボード完全ガイド |
| [ユーザー名バリエーションエンジン](wiki/Username-Variation-Engine.md) | バリエーション生成の仕組み |
| [GitNexus統合](wiki/GitNexus-Integration.md) | GitNexus の使用方法 |
| [FAQ](wiki/FAQ.md) | よくある質問 |

---

## クレジット

- **[Sherlock Project](https://github.com/sherlock-project/sherlock)** — オリジナルの OSINT ユーザー名列挙ツール
- **[GitNexus](https://gitnexus.dev)** — コードインテリジェンスエンジン：コールグラフ分析で9バグ発見、スパイダーウェブ可視化で Clue Web UI にインスピレーション
- **线索网 (Clue Web)** — GitNexus + Sherlock シナジーで構築

## ライセンス

本プロジェクトは [Sherlock](https://github.com/sherlock-project/sherlock) のフォークであり、[MIT ライセンス](LICENSE) の下で公開されています。
"""

# ─── BAHASA MELAYU ───────────────────────────────────────────────────

README_MS = HEADER + """\
<p align="center">
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>线索网</strong><br>
  <em>Alat siasatan OSINT visual yang memetakan jejak digital merentas 400+ platform<br>ke dalam papan perisikan web labah-labah interaktif.</em>
</p>

""" + LANG_SWITCHER_MS + DEMO_SECTION_MS + """
---

## Apa Itu 线索网 (Clue Web)?

Ini adalah **fork yang dipertingkatkan** daripada [Sherlock](https://github.com/sherlock-project/sherlock) — alat OSINT (Perisikan Sumber Terbuka) nama pengguna yang terkenal. Selain fungsi Sherlock asal, fork ini menambah:

1. **9 Pembaikan Bug** — dikenal pasti melalui kejuruteraan songsang pangkalan kod asal dengan enjin kecerdasan kod [GitNexus](https://gitnexus.dev) (2 kritikal, 5 sederhana, 1 bug, 1 minor)
2. **线索网 (Clue Web)** — alat penyiasatan visualisasi penuh, menghasilkan papan siasatan HTML interaktif, diilhamkan oleh antara muka graf web labah-labah GitNexus

---

## Bagaimana GitNexus dan Sherlock Bekerjasama

| Komponen | Peranan |
|----------|---------|
| **GitNexus** | Enjin kecerdasan kod — kejuruteraan songsang graf panggilan Sherlock, mengesan aliran pelaksanaan, mengenal pasti 9 bug dalam 3 fail. Visualisasi web labah-labahnya memberi inspirasi kepada reka bentuk UI Clue Web. |
| **Sherlock** (ditampal) | Enjin penghitungan nama pengguna teras — memeriksa 400+ platform. Fork ini merangkumi semua 9 pembaikan bug. |
| **线索网** | Lapisan visualisasi siasatan — mengambil output Sherlock dan memaparkannya sebagai graf nod interaktif dengan zum, seret, penapisan, pewarnaan kedalaman dan panel konteks. |

---

## Mula Pantas

```bash
# Klon fork ini
git clone https://github.com/verysleepylemon/sherlock.git
cd sherlock

# Cipta persekitaran maya
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate

# Pasang kebergantungan
pip install -e .

# Jalankan siasatan
python investigate.py <nama_pengguna>

# Contoh
python investigate.py john_doe
python investigate.py sleepy_lemonade --timeout 20
python investigate.py "my username" --max-variations 6 --no-browser
```

Papan siasatan HTML akan dibuka secara automatik dalam pelayar anda.

---

## Ciri-ciri 线索网 (Gaya GitNexus)

| Ciri | Penerangan |
|------|------------|
| **Zum dan Seret** | Roda tetikus untuk zum, seret klik kanan untuk menggerakkan |
| **Seret Nod** | Seret klik kiri mana-mana nod untuk mengubah kedudukan |
| **Pewarnaan Kesan Kedalaman** | BFS dari nod terpilih: d=1 cerah → d=2 sederhana → d=3+ malap (seperti radius impak GitNexus) |
| **Panel Konteks** | Klik mana-mana nod → panel kanan menunjukkan pandangan 360° (SASARAN / VARIASI / KATEGORI / LAMAN) |
| **Penapis Variasi** | Klik variasi nama pengguna → tunjuk platform variasi itu sahaja |
| **Togol Kategori** | Tunjuk/sembunyi keseluruhan kategori (Sosial, Permainan, Teknologi, Kreatif, Kewangan, Forum, Akademik, Lain-lain) |
| **Carian Masa Nyata** | Taip untuk malapkan nod yang tidak sepadan |
| **Peta Mini** | Peta mini kanan bawah, klik untuk teleport |
| **Serbuk Roti** | Bar bawah menunjukkan laluan boleh klik: Sasaran → Variasi → Kategori → Laman |
| **Eksport** | Satu klik salin semua URL ke papan keratan |
| **Pintasan Papan Kekunci** | `R` = muat pandangan, `Esc` = nyahpilih, `+/-` = zum, dwi-klik = set semula |
| **Mod Pandangan** | Web (lalai) / Radial / Fokus |
| **Tepi Beranimasi** | Animasi zarah pada sambungan yang diserlahkan |

---

## Bug yang Diperbaiki (9 Kesemuanya)

| # | Keterukan | Fail | Penerangan |
|---|-----------|------|------------|
| 1 | **KRITIKAL** | `sherlock.py` | Ketidakseragaman senarai/rentetan `errorType` — laman dengan senarai `errorType` menggunakan kaedah HTTP yang salah secara senyap (+29 platform tambahan dikesan) |
| 2 | **KRITIKAL** | `sherlock.py` | `response_text = r.text.encode()` menyebabkan ketidakpadanan bytes/str dalam semua perbandingan hiliran |
| 3 | **BUG** | `notify.py` | Off-by-one dalam `finish()` |
| 4 | **SEDERHANA** | `notify.py` | Pembilang global tidak selamat-benang |
| 5 | **SEDERHANA** | `sites.py` | Argumen lalai boleh ubah |
| 6 | **SEDERHANA** | `sites.py` | `username_unclaimed` sentiasa ditimpa oleh token rawak |
| 7 | **SEDERHANA** | `sherlock.py` | Logik argparse `--no-print-found` terbalik |
| 8 | **SEDERHANA** | `sherlock.py` | Pengesanan WAF ranap apabila respons `None` |
| 9 | **MINOR** | `sherlock.py` | Pengupasan awalan versi terlalu agresif |

---

## Enjin Variasi Nama Pengguna

Alat ini secara automatik menjana bentuk alternatif nama pengguna sasaran:

| Input | Variasi yang Dijana |
|-------|-------------------|
| `sleepy_lemonade` | `sleepy_lemonade`, `sleepylemonade`, `sleepy.lemonade`, `sleepy-lemonade`, `sleepyLemonade`, `SleepyLemonade`, `lemonade_sleepy`, `lemonadesleepy` |

Setiap variasi dicari merentas 400+ platform, keputusan dinyahduplikat, dan penemuan gabungan divisualkan dalam 线索网.

---

## Pilihan CLI

| Bendera | Lalai | Penerangan |
|---------|-------|------------|
| `username` | (wajib) | Nama pengguna sasaran untuk disiasat |
| `--timeout` | `10` | Tamat masa setiap laman dalam saat |
| `--max-variations` | `8` | Bilangan maksimum variasi nama pengguna |
| `--no-browser` | `false` | Jangan buka keputusan HTML secara automatik |

---

## Struktur Projek

```
sherlock/
├── investigate.py              # Pelari siasatan 线索网
├── clue_web_template.html      # Templat visualisasi gaya GitNexus
├── assets/
│   ├── banner.png              # Sepanduk repositori
│   ├── demo_terminal.gif       # Demo output terminal
│   └── clue_web_ui.png         # Tangkapan skrin UI
├── sherlock_project/
│   ├── sherlock.py             # Enjin teras (5 bug diperbaiki)
│   ├── notify.py               # Pemberitahuan hasil (2 bug diperbaiki)
│   ├── sites.py                # Definisi laman (2 bug diperbaiki)
│   └── resources/
│       └── data.json           # 400+ definisi platform
├── wiki/                       # Dokumentasi terperinci
├── README.md                   # English
├── README.zh-CN.md             # 简体中文
├── README.zh-TW.md             # 繁體中文
├── README.ja.md                # 日本語
└── README.ms.md                # Bahasa Melayu (fail ini)
```

---

## Dokumentasi

| Halaman | Penerangan |
|---------|------------|
| [Seni Bina](wiki/Architecture.md) | Seni bina sistem, jenis nod, aliran data |
| [Butiran Pembaikan Bug](wiki/Bug-Fixes-Detailed.md) | Analisis mendalam semua 9 bug |
| [Panduan UI Clue Web](wiki/Clue-Web-UI-Guide.md) | Panduan penuh papan siasatan |
| [Enjin Variasi Nama Pengguna](wiki/Username-Variation-Engine.md) | Cara variasi dijana |
| [Integrasi GitNexus](wiki/GitNexus-Integration.md) | Cara GitNexus digunakan |
| [Soalan Lazim](wiki/FAQ.md) | Soalan Lazim |

---

## Penghargaan

- **[Sherlock Project](https://github.com/sherlock-project/sherlock)** — Alat penghitungan nama pengguna OSINT asal
- **[GitNexus](https://gitnexus.dev)** — Enjin kecerdasan kod: analisis graf panggilan menemui 9 bug, visualisasi web labah-labah mengilhamkan UI Clue Web
- **线索网 (Clue Web)** — Dibina dengan sinergi GitNexus + Sherlock

## Lesen

Projek ini adalah fork daripada [Sherlock](https://github.com/sherlock-project/sherlock), dilesenkan di bawah [Lesen MIT](LICENSE).
"""

# ─── Write all files ─────────────────────────────────────────────────

files = {
    "README.md": README_EN,
    "README.zh-CN.md": README_ZH_CN,
    "README.zh-TW.md": README_ZH_TW,
    "README.ja.md": README_JA,
    "README.ms.md": README_MS,
}

for name, content in files.items():
    path = DIR / name
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {name} ({len(content):,} bytes)")

print(f"\nDone — {len(files)} README files written.")
