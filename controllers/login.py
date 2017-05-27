#login.py
from flask import *
from extensions import connect_to_database
import datetime, hashlib
db = connect_to_database()

login = Blueprint('login', __name__, template_folder='templates')

def query(query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()

@login.route('/login', methods=['GET'])
def login_route():
		return render_template("login.html")

@login.route('/api/v1/login', methods=['POST'])
def login_api_route():
        json_info = request.get_json()

        username = ''
        password = ''

        if 'username' in json_info and 'password' in json_info:
            username = json_info["username"]
            password = json_info["password"]
        else:
            json_errors = {
                "errors": [{"message": "You did not provide the necessary fields"}]
            }

            return jsonify(json_errors), 422

        passFromDB = ''

        user_data = query("SELECT * FROM User Where username = '" + username + "'")

        if user_data:
            passFromDB = user_data[0]['password']
        else:
            json_errors = {
                "errors": [{"message": "Username does not exist"}]
            }
            return jsonify(json_errors), 404

        m = hashlib.new('sha512')
        m.update(str(password).encode('utf-8'))
        password_to_check = m.hexdigest()

        if passFromDB == password_to_check:
            session['username'] = username

            return jsonify(username=username)
        else:
            json_error = {
                "errors": [{"message": "Password is incorrect for the specified username"}]
            }
            return jsonify(json_error), 422


@login.route('/api/v1/logout', methods=['POST'])
def logout_api_route():
    if 'username' in session:
        session.pop('username', None)
        return jsonify(''), 204
    else:
        json_error = {
            "errors": [{"message": "You do not have the necessary credentials for the resource"}]
        }
        return jsonify(json_error), 401

#@login.route('/logout', methods=['GET', 'POST'])
#def logout_route():
#	if 'username' in session:
#		session.pop('username', None)
#		return redirect(url_for('main.main_route'))
#	else:
#		return redirect(url_for('login.login_route'))
