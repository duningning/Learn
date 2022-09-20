# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 18:36
# 文件   : app6_表单数据到模板.py
# IDE   : PyCharm
from flask import Flask, render_template, request
from werkzeug.wrappers.response import ResponseStream
'''
Flask 将表单数据发送到模板     
'''
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index6.html')

@app.route('/result',methods = ['post','GET'])
def result():
    if request.method == 'POST':
        rst = request.form
        return render_template("result6.html",result=rst)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5555,debug=True,threaded=True)