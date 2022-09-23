# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/22 18:17
# 文件   : app14_Sijax.py
# IDE   : PyCharm
import os
from flask import Flask, g, render_template
import flask_sijax
'''
Flask Sijax
'''
app = Flask(__name__)

path = os.path.join('.',os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

flask_sijax.Sijax(app)

@app.route("/")
def hello():
    return "Hello World!<br /><a href='/sijax'>Go to Sijax test</a>"

@flask_sijax.route(app, "/sijax")
def hello_sijax():
    def hello_handler(obj_response, hello_from, hello_to):
        obj_response.alert('Hello from %s to %s' % (hello_from,hello_to))
        obj_response.css('a', 'color','green')

    def goodbye_handler(obj_response):
        obj_response.alert('Goodbye, whoever you are.')
        obj_response.css('a','color','red')

    if g.sijax.is_sijax_request:
        print("11111111111111111")
        g.sijax.register_callback('say_hello',hello_handler)
        g.sijax.register_callback('say_goodbye',goodbye_handler)
        return g.sijax.process_request()
    else:
        print("2222222222222")
        return render_template('sijaxexample.html')

if __name__ == "__main__":
    app.run(port=5555,debug=True, threaded = True)


