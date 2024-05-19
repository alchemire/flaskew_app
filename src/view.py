#coding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

# ルートディレクトリにアクセスしたときの挙動
@app.route("/")
def index():
    # return "HELLO WORLD!"
    return render_template("index.html")

# エントリーポイント
if __name__ == "__main__":
    app.run()