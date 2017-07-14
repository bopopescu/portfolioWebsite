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
	if 'username' in session:
		options['logged_in'] = True
		options['user'] = session['username']

	data = query("SELECT * from Collections ORDER BY created_time DESC")
	options['collections'] = data

	slides = query("SELECT * FROM Images WHERE carousel = '0'")
	options['slides'] = slides
	return render_template("index.html", **options)
