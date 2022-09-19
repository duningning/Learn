# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 14:54
# 文件   : app3.py
# IDE   : PyCharm
from flask import Flask, render_template
'''
渲染 模板
'''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index21.html')

if __name__ == "__main__":
    app.run(debug=True,threaded =True)