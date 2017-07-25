#about.py
from flask import *
from extensions import query, authenticate
import datetime


about = Blueprint('about', __name__, template_folder='templates')


@about.route('/about')
def about_route():
	options = {
		"year": datetime.datetime.now().year
	}
	options = authenticate(options)
	data = query("SELECT * from Collections ORDER BY created_time DESC")
	options['collections'] = data
	return render_template("about.html", **options)
