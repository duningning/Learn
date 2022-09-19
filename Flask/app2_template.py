# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 14:29
# 文件   : app2.py
# IDE   : PyCharm
from flask import Flask, render_template
'''
Flask 模板
'''
app = Flask(__name__)

@app.route('/')
def index():
    t_int = 18
    t_str = 'curry'
    t_list = [1,5,4,3,2]
    t_dict ={'name': 'durant', 'age': 28}



if __name__ == "__main__":
    app.run(debug=True,threaded =True)