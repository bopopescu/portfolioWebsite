#main.py
from flask import *
from extensions import connect_to_database
import datetime
db = connect_to_database()

main = Blueprint('main', __name__, template_folder='templates')
def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

@main.route('/')
def main_route():
    options = {
        "year": datetime.datetime.now().year
    }
    data = query("SELECT * from Collections ORDER BY created_time DESC")
    options['collections'] = data
    return render_template("index.html", **options)
