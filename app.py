#app.py
from flask import Flask, render_template, session
import extensions
import controllers
import config
app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.register_blueprint(controllers.main)
app.register_blueprint(controllers.about)
app.register_blueprint(controllers.contact)
app.register_blueprint(controllers.display)
app.register_blueprint(controllers.login)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host=config.env['host'],port = config.env['port'], debug=True)
