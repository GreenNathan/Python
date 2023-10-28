from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.users_model import Users

@app.route('/')
def index():
        return redirect('/allUsers')


@app.route('/allUsers')
def allUsers():
        return render_template('allUsers.html', users=Users.get_all())



@app.route('/addUsers')
def addUser():
        return render_template('addUser.html')

@app.route('/displayUser/<int:user_id>')
def displayUser(user_id):
        return render_template('displayUser.html', user=Users.get_one(user_id))


@app.route('/process', methods=['POST'])
def process():
        Users.create(request.form)
        print(request.form)
        return redirect('/allUsers')

@app.route('/update', methods=['POST'])
def update():
    Users.update(request.form)
    print(request.form)
    return redirect('/allUsers')

@app.route('/editUser/<int:user_id>')
def editUser(user_id):
        return render_template('editUser.html', user=Users.get_one(user_id))


@app.route('/delete/<int:user_id>')
def delete(user_id):
        Users.delete(user_id)
        return redirect('/allUsers')