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
  <strong>Sherlock</strong> 🔍 + <strong>GitNexus</strong> 🕷️ = <strong>线索网</strong><br>
  <em>一个可视化 OSINT 调查工具，将数字足迹映射到 400+ 平台上，<br>生成交互式蛛网情报看板。</em>
</p>

<p align="center">
  <strong>🌐 其他语言版本：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-TW.md">🇹🇼 繁體中文</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>---

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
.venv\Scripts\activate
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
