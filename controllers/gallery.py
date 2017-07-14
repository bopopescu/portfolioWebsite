from flask import *
from extensions import connect_to_database
import datetime, hashlib, os, sys
from werkzeug.utils import secure_filename


db = connect_to_database()

gallery = Blueprint('gallery', __name__, template_folder='templates')

def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

@gallery.route('/gallery/<galleryId>')
def gallery_route(galleryId):
    options = {
		"year": datetime.datetime.now().year
	}
    return render_template("gallery.html", **options)
