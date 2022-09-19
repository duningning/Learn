# _*_coding:utf-8_*_
# 作者:duningning.ming
# 创建时间: 2022/7/19 16:25
# 文件   : flask_app.py.py
# IDE   : PyCharm
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    #server = hello('127.0.0.1', 5000, app)
    #server.serve_forever()
    app.run('127.0.0.1', 5000, app)