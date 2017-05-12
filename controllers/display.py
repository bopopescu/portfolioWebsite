#display.py
from flask import *
from extensions import connect_to_database
import datetime
db = connect_to_database()

display = Blueprint('display', __name__, template_folder='templates')

@display.route('/about')
def display_route():
    return render_template("display.html")
