# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/21 11:50
# 文件   : form12.py
# IDE   : PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, IntegerField, SubmitField, RadioField, SelectField
from wtforms import validators #有效性检查


class ContactForm(FlaskForm):
    name = StringField("Name Of Student",[validators.InputRequired("Please enter your name.")])
    Gender = RadioField("Gender", choices=[("M","Male"),("F","Female")])
    Address = TextAreaField("Address")

    email = StringField("Email",[validators.InputRequired("Please enter your email address,"),
        validators.Email("Please enter your email address.")])# 做了两个检查：1是要求输入，2是要求输入邮件地址

    Age = IntegerField("age")
    language = SelectField("Languages", choices = [("cpp","C++"),("py","Python")])

    submit = SubmitField("Send")
