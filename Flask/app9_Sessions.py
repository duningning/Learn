# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/20 14:07
# 文件   : app9_Sessions.py
# IDE   : PyCharm
from flask import Flask
from flask import render_template
from flask import request
from flask import session,redirect,url_for
'''
Flask Session(会话)
'''
app = Flask(__name__)
app.secret_key = '123456' #使用Session必须先开启secret_Key(密钥)

@app.route('/')
def index():
    if 'username'in session:
        user = session['username']
        return '登录用户名是：'+ user +'<br>'+"<b><a href='/logout'>点击这里注销</a></b>"
    return "您暂未登录，<br><a href='/login'><b>点击这里登录</b></a>"

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('index7.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5555,debug=True,threaded=True)