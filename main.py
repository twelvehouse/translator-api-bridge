# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
import json
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv
import os

# .envファイルの内容を読み込む
load_dotenv()

# 環境変数から読み込み
API_URL = os.getenv('API_URL')  # 翻訳APIのURL
HOST = os.getenv('HOST', '127.0.0.1')  # デフォルトは 127.0.0.1
PORT = int(os.getenv('PORT', 5000))  # デフォルトはポート5000
TARGET_LANG = os.getenv('TARGET_LANG', 'ja')  # デフォルトは日本語

app = Flask(__name__)

# 翻訳用のエンドポイント
@app.route('/translate', methods=['GET'])
def translate():
    # クエリパラメータから値を取得
    from_lang = request.args.get('from')  # 翻訳元の言語
    to_lang = request.args.get('to')      # 翻訳先の言語
    text = request.args.get('text')       # 翻訳したいテキスト

    # APIに送信するデータ
    data = {
        "text": text,
        "target_lang": to_lang
    }

    try:
        # 翻訳APIにPOSTリクエストを送信
        response = requests.post(API_URL, data=json.dumps(data))
        
        # 翻訳されたテキストを返却
        response_data = response.json().get("data")
        return response_data

    except Exception as e:
        return f"翻訳に失敗しました: {str(e)}"


if __name__ == '__main__':
    # サーバー開始ログを出力
    print(f"API Bridge from {API_URL} is running on http://{HOST}:{PORT}")

    # gevent の WSGI サーバーを使用
    http_server = WSGIServer((HOST, PORT), app)
    http_server.serve_forever()