# Strands Agents ツール集

このリポジトリは、[Strands Agents SDK](https://github.com/strands-agents/sdk-python)で利用可能なすべてのツールを実装したサンプルコードを提供します。Strands Agentsは、AIエージェントを数行のコードで構築するためのモデル駆動型アプローチを提供するオープンソースSDKです。

## 概要

このプロジェクトでは、Strands Agentsで利用可能なすべてのツールを一つのエージェントに統合し、それらの使用方法を実演しています。これにより、Strands Agentsの機能と可能性を包括的に理解することができます。

## 含まれるツール

このプロジェクトには以下のカテゴリのツールが含まれています：

### ファイル操作系ツール
- `editor`: 高度なファイル編集操作
- `file_read`: ファイルの読み込みと解析
- `file_write`: ファイルの作成と修正

### シェルとシステム系ツール
- `environment`: 環境変数の管理
- `shell`: シェルコマンドの実行

### コード実行系ツール
- `python_repl`: Pythonコードの実行

### Web・ネットワーク系ツール
- `http_request`: API呼び出し、Webデータ取得、ローカルHTTPサーバー呼び出し

### マルチモーダル系ツール
- `image_reader`: 画像の処理と分析
- `generate_image`: Amazon Bedrockを使ったAI画像生成
- `nova_reels`: Amazon Bedrockの Nova Reelsを使ったAI動画生成

### AWSサービス系ツール
- `use_aws`: AWSサービスとの対話

### ユーティリティ系ツール
- `calculator`: 数学的演算の実行
- `current_time`: 現在の日付と時刻の取得
- `load_tool`: 実行時に追加のツールを動的に読み込み

### RAG・メモリ系ツール
- `retrieve`: Amazon Bedrock Knowledge Basesからのデータ検索

### エージェント・ワークフロー系ツール
- `agent_graph`: エージェントのグラフの作成と管理
- `journal`: エージェントが管理・作業するための構造化タスクとログの作成
- `swarm`: 共有メモリを持つ複数のAIエージェントの調整
- `stop`: エージェントイベントループの強制停止
- `think`: エージェント推論の並列ブランチを作成して深い思考を実行
- `use_llm`: カスタムプロンプトで新しいAIイベントループを実行
- `workflow`: シーケンスワークフローのオーケストレーション

## セットアップ

### 前提条件
- Python 3.10以上
- [uv](https://github.com/astral-sh/uv) - 高速なPythonパッケージインストーラーおよび環境マネージャー

### インストール手順

1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/strands-tools.git
cd strands-tools
```

2. uvを使用して仮想環境を作成
```bash
uv venv
```

3. 必要なパッケージをインストール
```bash
uv pip install strands-agents strands-agents-tools
```

## 使用方法

uvを使用してメインスクリプトを実行します：

```bash
uv run python main.py
```

または、仮想環境を有効化してから実行することもできます：

```bash
# 仮想環境を有効化
source .venv/bin/activate  # Linuxまたは macOS
# または
.venv\Scripts\activate     # Windows

# スクリプトを実行
python main.py
```

このスクリプトは以下のタスクを実行します：
1. 現在の日付と時刻の取得
2. 数学的計算の実行
3. Pythonコードの作成と実行
4. ファイルシステムの操作
5. HTTP APIリクエストの実行

## カスタマイズ

`main.py`ファイルを編集して、特定のツールのみを使用したり、異なるプロンプトを試したりすることができます。例えば：

```python
# 特定のツールのみを使用する場合
selected_tools = [calculator, current_time, http_request]
agent = Agent(
    model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    tools=selected_tools,
    system_prompt="You are a helpful assistant with access to selected tools."
)
```

## 依存関係の管理

uvを使用して依存関係を管理することができます：

```bash
# 新しいパッケージを追加
uv pip install パッケージ名

# 依存関係を更新
uv pip install --upgrade パッケージ名

# 依存関係をrequirements.txtに出力
uv pip freeze > requirements.txt
```

## 注意事項

- 一部のツール（`python_repl`や`shell`など）は、セキュリティ上の理由から実行前に確認プロンプトが表示されます
- AWSサービスを使用するツールには、適切なAWS認証情報が必要です
- マルチモーダルツールを使用するには、対応するモデルへのアクセス権が必要です
- uvの詳細な使用方法については、[uv公式ドキュメント](https://github.com/astral-sh/uv)を参照してください

## 参考リンク

- [Strands Agents SDK](https://github.com/strands-agents/sdk-python)
- [Strands Agents ドキュメント](https://strandsagents.com/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [uv ドキュメント](https://github.com/astral-sh/uv)

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については[LICENSE](LICENSE)ファイルを参照してください。
