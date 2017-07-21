#about.py
from flask import *
from extensions import *
import datetime
db = connect_to_database()

about = Blueprint('about', __name__, template_folder='templates')
def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

@about.route('/about')
def about_route():
	options = {
		"year": datetime.datetime.now().year
	}
	options = authenticate(options)
	data = query("SELECT * from Collections ORDER BY created_time DESC")
	options['collections'] = data
	return render_template("about.html", **options)
