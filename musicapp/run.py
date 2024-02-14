from musicapp import create_app, database
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from flask_cors import CORS
from musicapp.my_api import my_api_views

app = create_app()
CORS(app)


app.url_map.strict_slashes = False
app.register_blueprint(my_api_views)

@app.teardown_appcontext
def tear(self):
    """Tear down app context"""
    database.session.remove()

@app.route('/')
def index():
    return redirect(url_for('home.home_page'))



if __name__ == "__main__":
    app.app_context().push()
    app.run(debug=True)
