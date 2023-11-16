
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.shows_model import Shows



@app.route('/display/<int:shows_id>')
def display(shows_id):
    return render_template('display.html', show = Shows.get_one(shows_id))

# @app.route('/edit')
# def edited():
#     return render_template('edit.html')



@app.route('/addshow')
def addshow():
    return render_template('addshow.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: 
        return redirect('/login')
    return render_template('dashboard.html', shows = Shows.get_all())

@app.route('/createshow', methods=['POST'])
def createshow():
    if not Shows.validated(request.form):
        return redirect('/addshow')
    Shows.createshow(request.form)
    print(request.form)
    return redirect('/dashboard')

@app.route('/edit/<int:shows_id>')
def edit(shows_id):

    return render_template('edit.html', show = Shows.get_one(shows_id))
    
@app.route('/update', methods=['POST'])
def updateshow():
    if not Shows.validated(request.form):
        return redirect(f'/edit/{request.form["id"]}')
    Shows.update(request.form)
    print(request.form)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    Shows.delete(id)
    print('deleted')
    return redirect('/dashboard')