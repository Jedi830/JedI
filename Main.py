from flask import Flask, render_template, request, redirect, g
import pymysql

import flask_login

app = Flask(__name__)
app.secret_key = "Jedaiah"

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

def connect_db():
    return pymysql.connect(
        host="10.100.33.60",
        user="jdelacruz",
        password="229770375",
        database="jdelacruz_erdiagram",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
)

def get_db():
    """Opens a new database connection per request"""
    if not hasattr(g, "db"):
        g.db = connect_db()
    return g.db

@app.teardown_appcontext
def close_db(error):
    '''Closes the database connection at the end of request.'''    
    if hasattr(g, 'db'):
        g.db.close()

class User:
    is_authenticated = True
    is_anonymous = False
    is_active = True

    def __init__(self, id, username):

        self.username = username
        self.id = id
    
    def get_id(self):

        return str(self.id)

@app.route('/')
def index():
    user_name=""
    return render_template(
        "home.html.jinja",user_name=user_name
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["password"]
        cursor = get_db.cursor()
        cursor.execute(f"INSERT INTO `Users` (`Username`,`Password`) VALUES ('{username}', '{password}')")
        cursor.close()
        get_db.commit()
    
    return render_template("register.html.jinja")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Do this for every input in your form
        username = request.form["username"]
        password = request.form["password"]
        cursor = get_db.cursor()
        cursor.execute(f" Select * FROM `Users` WHERE `Username = `{username}`")
        User=cursor.fetchone()
        cursor.close()
        get_db.commit()
        if password==User["password"]:
            return redirect('/feed')

    return render_template("register.html.jinja")


@login_manager.user_loader
def load_user(user_id):
    cursor = get_db.cursor()

    cursor.execute(f"(SELECT * FROM `users` WHERE `id` = {user_id})")

    result = cursor.fetchone()

    cursor.close()

    get_db.commit()

    if result is None:
        return None

    return User(result["id"], result["username"])


@app.route('/feed')
@flask_login.login_required
def post_feed():
   return 'feed page'

@app.route('/post', methods=['POST'])
def create_post():
    description = request.form['description']
    user_id = flask_login.current_user.id()

    cursor = get_db.cursor()

    cursor.execute("INSERT INTO 'posts" ('descption', 'user_id'))


