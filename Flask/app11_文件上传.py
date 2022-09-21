# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/21 10:55
# 文件   : app11_文件上传.py
# IDE   : PyCharm
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename #将可能有异常的文件名转换成安全的文件名
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploaddir/'

@app.route('/')
def upload_file():
    return render_template('upload11.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file11'] #拿到提交的文件
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))#保存文件到
        return 'file uploaded successfully'

    elif request.method == 'GET':
        return render_template('upload11.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True, threaded=True)