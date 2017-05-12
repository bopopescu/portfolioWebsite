#contact.py
from flask import *
from extensions import connect_to_database
import datetime
db = connect_to_database()

contact = Blueprint('contact', __name__, template_folder='templates')

@contact.route('/about')
def contact_route():
    return render_template("contact.html")
