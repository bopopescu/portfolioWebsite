#about.py
from flask import *
from extensions import connect_to_database
import datetime
db = connect_to_database()

about = Blueprint('about', __name__, template_folder='templates')

@about.route('/about')
def about_route():
    return render_template("about.html")
