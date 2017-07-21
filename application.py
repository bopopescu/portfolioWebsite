#application.py
from flask import Flask, render_template, session
import extensions
import controllers
import config
from key import key
application = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = 'static/images'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


application.register_blueprint(controllers.main)
application.register_blueprint(controllers.about)
application.register_blueprint(controllers.contact)
application.register_blueprint(controllers.login)
application.register_blueprint(controllers.collection)
application.register_blueprint(controllers.gallery)

application.secret_key = key


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    application.run(host=config.env['host'],port = config.env['port'], debug=True)
