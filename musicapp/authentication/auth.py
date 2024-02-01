import secrets
from musicapp.authentication import auth_views
from musicapp import login_manager, database, mail
from flask_mail import Message
from musicapp.models.user import User
from flask_login import login_user, logout_user
from flask import render_template, request, abort, redirect, url_for, flash, current_app


@auth_views.route('/login', methods=['GET'])
def login():
    """login route"""
    #if request.arg.get('signup'):
    return render_template('login.html')

@auth_views.route('/login', methods=['POST'])
def post_login():
    user = User.query.filter(User.email == request.form.get('email')).first()
    if not user:
        flash('username or password not valid, please try again', 'error')
        return redirect(url_for('auth_views.login'))
    if not user.verify_password(request.form.get('password')):
        flash('username or password not valid, please try again', 'error')
        return redirect(url_for('auth_views.login'))

    login_user(user)
    
    if request.form.get('next'):
        return redirect(request.form.get('next'))
    
    flash('you have successfully login', 'success')
    return redirect(url_for('index'))

@auth_views.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You have logged out!', 'info')
    return redirect(url_for('auth_views.login'))

@auth_views.route('/signup', methods=['GET'])
def register():
    error = None
    return render_template('register.html', error=error)

@auth_views.route('/signup', methods=['POST'])
def post_register():
    error = False
    email_exists = User.query.filter(User.email == request.form.get('email')).first()
    if email_exists:
        flash('email already exists', 'error')
        error=True
    username_exists = User.query.filter(User.username == request.form.get('username')).first()
    if username_exists:
        flash('username already exists', 'error')
        error = True
    if request.form.get('password') != request.form.get('password_confirm'):
        flash('passwords don\'t match', 'error')
        error=True

    if error:
        return redirect(url_for('auth_views.register'))
    user = User(email=request.form.get('email'), username=request.form.get('username'), password=request.form.get('password'))
    database.session.add(user)
    database.session.commit()
    flash('user successfully registered, Please login now', 'success')
    return redirect(url_for('auth_views.login'))

@auth_views.route('/reset_password', methods=['GET'])
def reset_password():
    return render_template('reset_password.html', next=request.args.get('next'))


@auth_views.route('/reset_password', methods=['POST'])
def post_reset_password():
    user = User.query.filter_by(email=request.form.get('reset_email')).first()
    if not user:
        flash("Email does not exist", 'error')
        return redirect(url_for('auth_views.reset_password'))
    token = secrets.token_urlsafe(16)
    user.reset_token = token
    msg = Message('Reset your password',
            recipients=[user.email])
    msg.html = current_app.config['RESET_TEMPLATE'].format(user.username, url_for('auth_views.confirm_password_reset',
                  confirm_token=token, _external=True))
    mail.send(msg)
    database.session.commit()
    flash("Email reset request has been sent to your email. please check inbox to confirm reset", 'success')
    return redirect(url_for('auth_views.reset_password'))

@auth_views.route('/confirm_password_reset/<confirm_token>', methods=['GET'])
def confirm_password_reset(confirm_token=''):
    token_exists = User.query.filter_by(reset_token=confirm_token).first()
    if not token_exists:
        return abort(401)
    return render_template('new_password.html', reset_token=token_exists.reset_token)


@auth_views.route('/confirm_password', methods=['POST'])
def post_confirm_password():
    if request.form.get('new_password') != request.form.get('new_password_confirm'):
        flash("Passwords don't match", 'error')
        return render_template('new_password.html', token=request.form.get('reset_token'))
    user = User.query.filter_by(reset_token=request.form.get('reset_token')).first()
    user.password = request.form.get('new_password')
    user.reset_token = ''
    database.session.commit()
    flash("Your password has been reset successfully", 'success')
    return redirect(url_for('auth_views.login'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('auth_views.login', next=request.path))

