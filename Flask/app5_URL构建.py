# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 18:11
# 文件   : app5_URL构建.py
# IDE   : PyCharm
from flask import Flask,redirect,url_for
'''
Flask URL构建
'''
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'hi admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))#根据判断条件跳转设定的url
    else:
        return redirect(url_for('hello_guest',guest = name))


if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True,threaded=True)
