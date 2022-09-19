# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 12:18
# 文件   : app1.py.py
# IDE   : PyCharm
from flask import Flask
'''
Flask 路由
'''
app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d'% postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f'% revNo

@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/python/') #url标准写法
def hello_python():
    return 'Hello python '

if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True,threaded=True)