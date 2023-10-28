#all routes

from flask import render_template, redirect, session, request
from flask_app import app

# from flask_app.models.users_model import Users


@app.route('/')
def index():
    return redirect('/showRecipe')

@app.route('/showRecipe')
def showRecipe():
    return render_template('/showRecipe.html')

@app.route('/recipeShare')
def recipeShare():
    return render_template('/recipeShare.html')

@app.route('/recipe')
def recipe():
    return render_template('/recipe.html')

@app.route('/newRecipe')
def newRecipe():
    return render_template('/newRecipe.html')

@app.route('/editRecipe')
def editRecipe():
    return render_template('/editRecipe.html')

# @app.route('/acceptLogin')
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