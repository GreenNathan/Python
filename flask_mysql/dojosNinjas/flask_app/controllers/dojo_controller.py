#all routes

from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo_model import Dojos


@app.route('/')
def index():
    return redirect('/allDojos')

@app.route('/allDojos')
def allDojos():
    return render_template('allDojos.html', dojos = Dojos.get_all())

@app.route('/create', methods=['POST'])
def createDojo():
        Dojos.create(request.form)
        print(request.form)
        return redirect('/allDojos')

@app.route('/update', methods=['POST'])
def updateDojo():
    Dojos.update(request.form)
    print(request.form)
    return redirect('/allDojos')

# @app.route('/addNinja')
# def addNinja():
#     return render_template('addNinja.html')

# @app.route('/newNinja/<int:user_id>')
# def newNinja(User_id):
#     return render_template('newNinja.html',) #user=Users.get_one(user_id))

@app.route('/delete/<int:user_id>')
def deleteDojo(user_id):
    Dojos.delete(user_id)
    return redirect('/newDojos')

@app.route('/dojos/<int:dojo_id>')
def viewdojo(dojo_id):
    return render_template('theNinjas.html', dojo = Dojos.get_one_with_ninjas(dojo_id))