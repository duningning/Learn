# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/19 14:54
# 文件   : app3.py
# IDE   : PyCharm
from flask import Flask, render_template
'''
渲染 模板
'''
app = Flask(__name__)

@app.route('/')
def index():
    t_int = 18
    t_str = 'curry'
    t_list = [2,5,4,3,2]
    t_dict ={'name': 'durant', 'age': 28}
    #render_template方法：渲染模板
    #参数1： 模板名称 参数n:传到模板里的数据
    return render_template('index3.html',
                           my_int = t_int,
                           my_str = t_str,
                           my_list = t_list,
                           my_dict = t_dict)


if __name__ == "__main__":
    app.run(debug=True,threaded =True)