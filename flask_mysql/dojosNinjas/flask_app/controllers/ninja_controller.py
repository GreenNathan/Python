#all routes

from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.ninja_model import Ninjas
from flask_app.models.dojo_model import Dojos

@app.route('/newNinja')
def addNinja():
    return render_template('newNinja.html', dojos = Dojos.get_all())

@app.route('/theNinjas', methods=['POST'])
def updateNinja():
    Ninjas.update(request.form)
    print(request.form)
    return redirect('/allDojos')

@app.route('/processNinja', methods=['POST'])
def processNinja():
        Ninjas.create(request.form)
        print(request.form)
        return redirect('/allDojos')


@app.route('/newNinja/<int:user_id>')
def newNinja(User_id):
    return render_template('newNinja.html',) #user=Users.get_one(user_id))


@app.route('/delete/<int:user_id>')
def deleteNinja(user_id):
    Ninjas.delete(user_id)
    return redirect('/allDojos')