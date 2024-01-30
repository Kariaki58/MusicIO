from musicapp.authentication import auth_views
from musicapp import login_manager, database
from musicapp.models.user import User
from flask_login import login_user, logout_user
from flask import render_template, request, redirect, url_for, flash


@auth_views.route('/login', methods=['GET'])
def login():
    """login route"""
    #if request.arg.get('signup'):
    return render_template('login.html')

@auth_views.route('/login', methods=['POST'])
def post_login():
    user = User.query.filter(User.email == request.form.get('email')).first()
    if not user:
        flash('username or password not valid, please try again', category='error')
        return redirect(url_for('auth_views.login'))
    if not user.verify_password(request.form.get('password')):
        flash('username or password not valid, please try again', category='error')
        return redirect(url_for('auth_views.login'))

    login_user(user)
    
    flash('you have successfully login', 'success')
    return redirect(url_for('home.home_page'))

@auth_views.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You have logged out!', category='info')
    return redirect(url_for('auth_views.login'))

@auth_views.route('/signup', methods=['GET'])
def register():
    error = None
    return render_template('register.html', error=error)

@auth_views.route('/signup', methods=['POST'])
def post_register():
    error = False
    email_exists = User.query.filter(User.email == request.form.get('email')).first()
    username_exists = User.query.filter(User.username == request.form.get('username')).first()
    if email_exists:
        flash('email already exists', category='error')
        error=True
    elif username_exists:
        flash('username already exists', category='error')
        error = True
    elif request.form.get('password') != request.form.get('password_confirm'):
        flash('passwords don\'t match', category='error')
        error=True

    if error:
        return redirect(url_for('auth_views.register'))
    user = User(email=request.form.get('email'), username=request.form.get('username'), password=request.form.get('password'))
    database.session.add(user)
    database.session.commit()
    flash('user successfully registered, Please login now', category='success')
    return redirect(url_for('auth_views.login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

