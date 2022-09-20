# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/20 15:29
# 文件   : app10_消息闪现.py
# IDE   : PyCharm
from flask import Flask, flash, redirect, render_template, request, url_for
'''
Flask 消息闪现
'''
app =Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    return render_template('index10.html')

@app.route('/login', methods= ['GET','POST'])
def login():
    errormsg = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            errormsg = 'Invalid username or password. Please  try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('login10.html',error = errormsg)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5555, debug=True, threaded=True)