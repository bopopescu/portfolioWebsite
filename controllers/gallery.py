from flask import *
from extensions import query, authenticate
import datetime, hashlib, os, sys
from werkzeug.utils import secure_filename




gallery = Blueprint('gallery', __name__, template_folder='templates')


@gallery.route('/gallery/<collection>')
def gallery_route(collection):
	options = {
		"year": datetime.datetime.now().year
	}
	options = authenticate(options)

	data = query("SELECT * from Collections ORDER BY created_time;")
	images = query("SELECT * FROM Images WHERE collection =\"" + str(collection) + "\" ORDER BY created_time;")
	options['collections'] = data
	options['images'] = images
	return render_template("gallery.html", **options)
