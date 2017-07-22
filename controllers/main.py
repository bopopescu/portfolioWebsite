#main.py
from flask import *
from extensions import *
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
	options = authenticate(options)
	data = query("SELECT * from Collections ORDER BY created_time ")
	options['collections'] = data

	slides = query("SELECT * FROM Images WHERE carousel = '0' ORDER BY created_time")
	options['slides'] = slides
	return render_template("index.html", **options)
