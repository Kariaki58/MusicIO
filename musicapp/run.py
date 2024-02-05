from musicapp import create_app, database
from flask import render_template
from flask_login import current_user, login_required
from musicapp.authentication import auth_views
from musicapp.api import api_views

app = create_app()
app.url_map.strict_slashes = False
app.register_blueprint(auth_views)
app.register_blueprint(api_views)

@app.teardown_appcontext
def tear(self):
    """Tear down app context"""
    database.session.remove()

@app.route('/')
@login_required
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.app_context().push()
    app.run(debug=True)
