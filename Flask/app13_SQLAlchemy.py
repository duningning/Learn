# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/22 10:17
# 文件   : app13_SQLAIchemy&数据库.py
# IDE   : PyCharm
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, RadioField, SelectField, HiddenField

from wtforms import validators
'''
Flask SQLAlchemy
'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SECRET_KEY'] = '123456'

db = SQLAlchemy(app)

class ContactDAO(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(1))
    address = db.Column(db.String(100))
    email = db.Column(db.String(50))
    age = db.Column(db.Integer)
    language = db.Column(db.String(5))
    date_created = db.Column(db.DateTime,default = datetime.now)

    def __init__(self, name, gender, address, email, age, language):
        self.name = name
        self.gender = gender
        self.address = address
        self.email = email
        self.age = age
        self.language = language

class ContactForm(FlaskForm):
    id = HiddenField("id")
    name = StringField("Name of Student",[validators.InputRequired("Please enter your name.")])
    Gender = RadioField("Gender", choices = [("M","Male"),("F","Female")])
    Address = TextAreaField("Address")

    email = StringField("Email",[validators.InputRequired("Please enter your email address,"),
        validators.Email("Please enter your email address.")])# 做了两个检查：1是要求输入，2是要求输入邮件地址

    Age = IntegerField("age")
    language = SelectField("Languages", choices=[("cpp", "C++"), ("py", "Python")])

    submit = SubmitField("Send")

@app.route("/")
def show_all():
    return render_template("show13.html", contacts = ContactDAO.query.all())

@app.route("/add", methods = ["post", "GET"])
def do_add():
    form1 = ContactForm()
    if request.method == "POST":
        if form1.validate() == False:
            flash("All fields are required.")
            return render_template("add13.html", form = form1)
        else:
            contact = ContactDAO(form1.name.data,
                                 form1.Gender.data,
                                 form1.Address.data,
                                 form1.email.data,
                                 form1.Age.data,
                                 form1.language.data)
            try:
                db.session.add(contact)
                db.session.commit()
                flash("Record was successfully added")
                return redirect("/")
            except Exception as e:
                flash("There is an issue adding contact into db. {0}".format(e))
                return render_template("add13.html",form = form1)

    elif request.method == "GET":
        return render_template("add13.html", form = form1)

@app.route("/delete/<int:id>")
def do_delete(id):
    to_delete = ContactDAO.query.get_or_404(id)
    try:
        db.session.delete(to_delete)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        flash("There is an issue delete contact into db. {0}".format(e))
        return redirect("/")

@app.route("/update/<int:id>", methods = ["POST","GET"])
def do_update(id):
    form1 = ContactForm()
    to_update = ContactDAO.query.get_or_404(id)

    if request.method == "GET":
        form1.id.data = to_update.id
        form1.name.data = to_update.name
        form1.Gender.data = to_update.gender
        form1.Address.data = to_update.address
        form1.Age.data = to_update.age
        form1.language.data = to_update.language
        return render_template("update13.html",form = form1)

    elif request.method == "POST":
        to_update.id = id
        to_update.name = form1.name.data
        to_update.gender = form1.Gender.data
        to_update.address = form1.Address.data
        to_update.email = form1.email.data
        to_update.age = form1.Age.data
        to_update.language = form1.language.data
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            flash("There is an issue update contact into db. {0}".format(e))
            return redirect("/")

if __name__ == "__main__":
    app.run(port=5555,debug=True, threaded = True)

