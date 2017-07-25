#contact.py
from flask import *
from extensions import query, authenticate
import datetime

contact = Blueprint('contact', __name__, template_folder='templates')


@contact.route('/contact')
def contact_route():
	options = {
		"year": datetime.datetime.now().year
	}
	options = authenticate(options)
	data = query("SELECT * from Collections ORDER BY created_time DESC")
	options['collections'] = data
	return render_template("contact.html", **options)
