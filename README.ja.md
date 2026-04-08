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
  <em>400以上のプラットフォームにわたるデジタルフットプリントを<br>インタラクティブなスパイダーウェブ情報ボードに可視化するOSINT調査ツール。</em>
</p>

<p align="center">
  <strong>🌐 他の言語版：</strong><br>
  <a href="README.md">🇬🇧 English</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.zh-TW.md">🇹🇼 繁體中文</a> ·
  <a href="README.ms.md">🇲🇾 Bahasa Melayu</a>
</p>---

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
.venv\Scripts\activate
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
