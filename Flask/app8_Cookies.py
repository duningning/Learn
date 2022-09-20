# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/20 11:55
# 文件   : app8_Cookies.py
# IDE   : PyCharm
from flask import Flask, make_response,request
'''
Flask Cookies
'''
app = Flask(__name__)

@app.route('/set_cookies')
def set_cookie():
    resp = make_response('success')
    resp.set_cookie('aaa_key','aaa_value',max_age=3600)
    return resp

@app.route('/get_cookies')
def get_cookie():
    cookie_1 = request.cookies.get('aaa_key')
    return cookie_1

@app.route('/delete_cookies')
def delete_cookie():
    resp = make_response('del_success')
    resp.delete_cookie('aaa_key')
    return resp

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5555,debug=True,threaded=True)