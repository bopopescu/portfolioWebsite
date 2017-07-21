#contact.py
from flask import *
from extensions import *
import datetime
db = connect_to_database()

contact = Blueprint('contact', __name__, template_folder='templates')
def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

@contact.route('/about')
def contact_route():
	options = {
		"year": datetime.datetime.now().year
	}
	options = authenticate(options)
	data = query("SELECT * from Collections ORDER BY created_time DESC")
	options['collections'] = data
	return render_template("contact.html", **option)
