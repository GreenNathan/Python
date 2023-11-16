#all routes

# from flask import render_template, redirect, session, request
# from flask_app import app
# from flask_app.models.users_model import Users

from flask import render_template, redirect, session, request, flash
from flask_app import app, bcrypt
from flask_app.models.user_model import Users


@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/create', methods=['POST'])
def create():
    if not Users.validate(request.form):
        return redirect('/login')
    user_data = {

        **request.form,
        'pw_hash': bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = Users.create(user_data)
    session['user_id'] = user_id
    print(session['user_id'])
    session['first_name'] = request.form['first_name']
    print(request.form)
    print(session['user_id'])
    return redirect('/dashboard')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash('You have been logged out.', 'success_logout')
    return redirect('/login')

@app.route('/accept_login', methods=['POST'])
def accept_login():

    user = Users.login_user(request.form)
    if user:
        session['user_id'] = user.id
        session['first_name'] = user.first_name
        return redirect('/dashboard')
    else:
        return redirect('/login')













# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass

# @app.route('/')
# def index():
#     pass