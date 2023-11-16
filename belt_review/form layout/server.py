from flask_app import app

                                #"users"(controller name)
from flask_app.controllers import users_controller


if __name__ == "__main__":
        app.run(debug=True)


# pipenv shell
# pipenv install flask PyMySQL flask-bcrypt