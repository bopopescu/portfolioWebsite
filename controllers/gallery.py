from flask import *
from extensions import *
import datetime, hashlib, os, sys
from werkzeug.utils import secure_filename


db = connect_to_database()

gallery = Blueprint('gallery', __name__, template_folder='templates')

def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

@gallery.route('/gallery/<collection>')
def gallery_route(collection):
	options = {
		"year": datetime.datetime.now().year
	}
	options = authenticate(options)

	data = query("SELECT * from Collections ORDER BY created_time")
	images = query("SELECT * FROM Images WHERE collection =\"" + str(collection) + "\" ORDER BY created_time;")
	options['collections'] = data
	options['images'] = images
	return render_template("gallery.html", **options)
