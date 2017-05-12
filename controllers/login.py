#login.py
from flask import *
from extensions import connect_to_database
import datetime
db = connect_to_database()

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/about')
def login_route():
    return render_template("login.html")
