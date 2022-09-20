# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/20 10:39
# 文件   : app7_重定向和错误.py
# IDE   : PyCharm
from flask import Flask, redirect, url_for, render_template, request, abort
'''
Flask 重定向和错误
'''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index7.html')

@app.route('/login',methods= ['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    elif request.method == 'GET':
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5555,debug=True,threaded=True)