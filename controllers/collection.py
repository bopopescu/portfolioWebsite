from flask import *
from extensions import connect_to_database
import datetime, hashlib, os, sys
from werkzeug.utils import secure_filename


db = connect_to_database()

collection = Blueprint('collection', __name__, template_folder='templates')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@collection.route('/create_collection', methods=['GET','POST'])
def create_collection_route():
	options = {
		"year": datetime.datetime.now().year
	}
	if request.method == 'GET':
		data = query("SELECT * from Collections ORDER BY created_time DESC")
		options['collections'] = data
		return render_template("addCollect.html", **options)
	elif request.method == 'POST':
		new_collection = request.form['new_collection']
		m = hashlib.new('md5')
		m.update(str(new_collection).encode('utf-8'))
		query("INSERT INTO Collections(title, size) values ('" + new_collection + "'" + ",'" + str(0) + "')")
		data = query("SELECT * from Collections ORDER BY created_time DESC")
		options['collections'] = data
		return render_template("addCollect.html", **options)
	else:
		return render_template("404.html")

@collection.route('/edit_collection', methods=['GET','POST'])
def edit_collection_route():
	options = {
		"year": datetime.datetime.now().year
	}
	collection = request.args.get('collection')

	if request.method == 'GET':
		img_data = query("SELECT * from Images WHERE collection = '"+ collection + "'")
		options['images'] = img_data
		return render_template("editCollection.html", **options)
	elif request.method == 'POST':
		if request.form['op'] == 'add':
			file = request.files['file']
			if file.filename != '':
				if file and allowed_file(file.filename):
					m = hashlib.md5((file.filename + collection + str(datetime.datetime.now())).encode('utf-8'))
					hashed = m.hexdigest()
					get_extension = file.filename.rsplit('.', 1)[1].lower()
					new_filename = hashed + "." + get_extension
					filename = secure_filename(new_filename)
					carousel = '0'
					file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
					query("INSERT INTO Images(id, format, collection, carousel) VALUES ('"+hashed+"', '"+get_extension+"','" + collection + "','" + carousel + "')")
		return redirect(url_for('collection.edit_collection_route', collection=collection))
