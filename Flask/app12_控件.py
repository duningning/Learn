# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/21 11:47
# 文件   : app12_控件.py
# IDE   : PyCharm
from flask import Flask, render_template, request, flash
from Flask.form12 import ContactForm
'''
Flask WTF
'''
app = Flask(__name__)
app.secret_key = '123456'

@app.route('/',methods =['GET','POST'])
def contact():
    form1 = ContactForm()

    if request.method == 'POST':
        if form1.validate() == False:
            flash('All fields are required')
            return render_template('contact12.html',form =form1)
        else:
            return render_template('success12.html')

    elif request.method == 'GET':
        return render_template('contact12.html',form = form1)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5555,debug= True,threaded=True)
