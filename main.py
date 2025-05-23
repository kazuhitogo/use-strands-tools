from strands import Agent

# Strands Agentsで利用可能なすべてのツールをインポート
# ファイル操作系ツール
from strands_tools import editor        # 高度なファイル編集操作
from strands_tools import file_read     # ファイルの読み込みと解析
from strands_tools import file_write    # ファイルの作成と修正

# シェルとシステム系ツール
from strands_tools import environment   # 環境変数の管理
from strands_tools import shell         # シェルコマンドの実行

# コード実行系ツール
from strands_tools import python_repl   # Pythonコードの実行

# Web・ネットワーク系ツール
from strands_tools import http_request  # API呼び出し、Webデータ取得、ローカルHTTPサーバー呼び出し

# マルチモーダル系ツール
from strands_tools import image_reader  # 画像の処理と分析
from strands_tools import generate_image # Amazon Bedrockを使ったAI画像生成
from strands_tools import nova_reels    # Amazon Bedrockの Nova Reelsを使ったAI動画生成

# AWSサービス系ツール
from strands_tools import use_aws       # AWSサービスとの対話

# ユーティリティ系ツール
from strands_tools import calculator    # 数学的演算の実行
from strands_tools import current_time  # 現在の日付と時刻の取得
from strands_tools import load_tool     # 実行時に追加のツールを動的に読み込み

# RAG・メモリ系ツール
from strands_tools import retrieve      # Amazon Bedrock Knowledge Basesからのデータ検索

# エージェント・ワークフロー系ツール
from strands_tools import agent_graph   # エージェントのグラフの作成と管理
from strands_tools import journal       # エージェントが管理・作業するための構造化タスクとログの作成
from strands_tools import swarm         # 共有メモリを持つ複数のAIエージェントの調整
from strands_tools import stop          # エージェントイベントループの強制停止
from strands_tools import think         # エージェント推論の並列ブランチを作成して深い思考を実行
from strands_tools import use_llm       # カスタムプロンプトで新しいAIイベントループを実行
from strands_tools import workflow      # シーケンスワークフローのオーケストレーション

def main():
    """
    Strands Agentsの全ツールを使用したエージェントを作成し、その使用方法を実演します。
    """
    # デバッグログを有効化
    import logging
    logging.getLogger("strands").setLevel(logging.DEBUG)
    logging.basicConfig(
        format="%(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler()]
    )

    # 利用可能なすべてのツールをリストにまとめる
    all_tools = [
        # ファイル操作系ツール
        editor, file_read, file_write,
        
        # シェルとシステム系ツール
        environment, shell,
        
        # コード実行系ツール
        python_repl,
        
        # Web・ネットワーク系ツール
        http_request,
        
        # マルチモーダル系ツール
        image_reader, generate_image, nova_reels,
        
        # AWSサービス系ツール
        use_aws,
        
        # ユーティリティ系ツール
        calculator, current_time, load_tool,
        
        # RAG・メモリ系ツール
        retrieve,
        
        # エージェント・ワークフロー系ツール
        agent_graph, journal, swarm, stop, think, use_llm, workflow
    ]

    # ストリーミングイベントをキャプチャするコールバックハンドラを定義
    tool_use_ids = []
    def callback_handler(**kwargs):
        if "data" in kwargs:
            # ストリーミングデータのチャンクを表示
            print(kwargs["data"], end="", flush=True)
        elif "current_tool_use" in kwargs:
            tool = kwargs["current_tool_use"]
            if tool["toolUseId"] not in tool_use_ids:
                # ツール使用をログに記録
                print(f"\n[Using tool: {tool.get('name')}]")
                tool_use_ids.append(tool["toolUseId"])

    # エージェントを作成
    agent = Agent(
        # Amazon BedrockのClaude 3.7 Sonnetモデルを使用
        model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        
        # 全ツールを追加
        tools=all_tools,
        
        # システムプロンプトを設定
        system_prompt="You are a helpful assistant with access to many tools. Demonstrate how to use these tools effectively.",
        
        # ストリーミング用コールバックハンドラを追加
        callback_handler=callback_handler
    )

    # 複数のツールを活用するプロンプトの例
    prompt = """
    I need help with several tasks:
    
    1. What is the current date and time?
    2. Calculate 1234 * 5678
    3. Create a simple Python function that adds two numbers and test it
    4. List the files in the current directory
    5. Show me how to make an HTTP request to a public API
    
    For each task, explain which tool you're using and why it's appropriate.
    """
    
    # エージェントにプロンプトを送信して実行
    response = agent(prompt)
    
    # 最終的な応答を表示
    print("\n\nFinal response:")
    print(response.message)

# スクリプトが直接実行された場合にmain関数を実行
if __name__ == "__main__":
    main()
