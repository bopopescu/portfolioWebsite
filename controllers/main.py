#main.py
from flask import *
from extensions import connect_to_database
import datetime
db = connect_to_database()

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    options = {
        "year": datetime.datetime.now().year
    }
    return render_template("index.html", **options)
