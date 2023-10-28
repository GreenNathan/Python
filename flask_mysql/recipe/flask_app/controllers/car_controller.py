
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.cars_model import Cars

@app.route('/cars')
def loggedin():
    if 'user_id' not in session: 
        return redirect('/login')
    return render_template('loggedin.html', cars = Cars.get_all())

@app.route('/show/<int:cars_id>')
def displayinfo(cars_id):
    return render_template('show.html', car = Cars.get_one(cars_id))

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/forsale')
def forsale():
    return render_template('forsale.html')

@app.route('/createcar', methods=['POST'])
def createcar():
    Cars.createcar(request.form)
    print(request.form)
    return redirect('/cars')

@app.route('/update', methods=['POST'])
def updatecar():
    Cars.update(request.form)
    print(request.form)
    return redirect('/cars')

@app.route('/delete/<int:id>')
def delete(id):
    Cars.delete(id)
    print('deleted')
    return redirect('/cars')