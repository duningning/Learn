# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 16:37
# 文件   : app4_静态文件.py
# IDE   : PyCharm
from flask import Flask, render_template, url_for
'''
Flask 静态文件
'''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index4.html')

if __name__=="__main__":
    app.run(debug=True, threaded=True)