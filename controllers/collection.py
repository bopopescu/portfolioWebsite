from flask import *
from extensions import connect_to_database
import datetime, hashlib

db = connect_to_database()

collection = Blueprint('collection', __name__, template_folder='templates')

def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

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
    return render_template("editCollection.html", **options)
