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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Do this for every input in your form
        username = request.form["username"]
        password = request.form["password"]
        bio = request.form["bio"]
        birthday = request.form["birthday"]


        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO `user` ('Email','Username','Password','bio' ) VALUES ('{username}', '{password}', '{bio}')")
        cursor.close()
        connection.commit()
    
    return render_template("register.html.jinja")

connection = pymysql.connect(
    database = "jdelacruz_erdiagram",
    user = "jdelacruz",
    password = "229770375",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor,
)
