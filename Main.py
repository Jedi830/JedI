from flask import Flask, render_template, request, redirect
import pymysql
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

authentication = HTTPBasicAuth()
app = Flask(__name__)

@app.route('/')
def index():
    user_name=""
    return render_template(
        "home.html.jinja",user_name=user_name
    )

@app.route('/register')
def register():
    user_name1=""
    return render_template(
        "register.html.jinja",user_name=user_name1
    )