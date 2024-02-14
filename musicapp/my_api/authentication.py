from . import my_api_views
import secrets
from flask import request, jsonify, url_for, current_app
from musicapp import login_manager, database, mail
from flask_mail import Message
from musicapp.models.user import User
from flask_login import login_user, logout_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@my_api_views.route('/register', methods=['POST'])
def authentication_register():    
    api_data = request.json

    email = api_data['email']
    password = api_data['password']
    username = api_data['username']

    email_exists = User.query.filter_by(email=email).first()
    user_exists = User.query.filter_by(username=username).first()

    if email_exists:
        return jsonify({'message': 'email already exist'})

    if user_exists:
        return jsonify({'message': 'username already exist'})

    user_info = User(email=email, password=password, username=username)

    database.session.add(user_info)
    database.session.commit()
    
    return jsonify({'message': 'Registration successful'}), 201


@my_api_views.route('/login', methods=['POST'])
def authentication_login():
    api_data = request.json

    email = api_data['email']
    password = api_data['password']

    user = User.query.filter(User.email==email).first()
    
    if not user:
        return jsonify({'message': 'invalid email'})
    
    if user.verify_password(password):
        user = user.to_dict()
        save_user_dict = {}
        for data in user:
            if data == '_sa_instance_state':
                continue
            save_user_dict[data] = user[data]
    
        return jsonify([{'message': 'login sucessful'}, save_user_dict])
    return jsonify({'message': 'password don\'t match'})


@my_api_views.route('/reset_password', methods=['POST'])
def post_reset_password():
    user = User.query.filter_by(email=request.form.get('reset_email')).first()
    if not user:
        return jsonify({'message': 'Email don\'t exist'})
    token = secrets.token_urlsafe(16)
    user.reset_token = token
    msg = Message('Reset your password',
            recipients=[user.email])
    msg.html = current_app.config['RESET_TEMPLATE'].format(user.username, token)
    mail.send(msg)
    database.session.commit()
    return jsonify({'message': 'Email sent to your email'})

@my_api_views.route('/confirm_password_reset/<confirm_token>', methods=['GET'])
def confirm_password_reset(confirm_token=''):
    token_exists = User.query.filter_by(reset_token=confirm_token).first()
    if not token_exists:
        return jsonify({'message': 'token don\'t exist request a new one'})
    return jsonify({'message': 'set_password', 'reset_token': token_exists.reset_token})

@my_api_views.route('/confirm_password', methods=['POST'])
def post_confirm_password():
    if request.form.get('new_password') != request.form.get('new_password_confirm'):
        return jsonify({'message': "Passwrods don't match", token: request.form.get('reset_token')})
    user = User.query.filter_by(reset_token=request.form.get('reset_token')).first()
    user.password = request.form.get('new_password')
    user.reset_token = ''
    database.session.commit()
    return jsonify({'message': 'Your password has been reset successfully'})
