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
@app.route('/translate/<text>', methods=['GET'])
def translate(text):
    # APIに送信するデータ
    data = {
        "text": text,
        "target_lang": TARGET_LANG  # 環境変数から言語を取得
    }

    try:
        # 自作の翻訳APIにPOSTリクエストを送信
        response = requests.post(API_URL, data=json.dumps(data))
        
        # レスポンスをJSON形式に変換
        response_data = response.json().get("data")
        
        # 翻訳されたテキストを平文で返す
        return response_data

    except Exception as e:
        return f"翻訳に失敗しました: {str(e)}"


if __name__ == '__main__':
    # サーバー開始ログを出力
    print(f"API Bridge from {API_URL} is running on http://{HOST}:{PORT}")

    # gevent の WSGI サーバーを使用
    http_server = WSGIServer((HOST, PORT), app)
    http_server.serve_forever()