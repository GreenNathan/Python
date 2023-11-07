#class methods
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

from flask_app import app, bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




    @classmethod
    def login_user(cls, creds):
        
        found_user = cls.get_one_by_email(creds['email'])

        if found_user:
            if bcrypt.check_password_hash(found_user.pw_hash, creds['password']):
                
                return found_user
            else:
                flash('Invalid login attempt')
                return False
        else:
            flash('Invalid login attempt')
            return False




    @classmethod
    def create(cls, data):
        query = '''
                INSERT into users (first_name, last_name, email, pw_hash)
                VALUES (%(first_name)s, %(last_name)s, %(email)s,
                %(pw_hash)s)
                '''
        return connectToMySQL('log_in_db').query_db(query, data)

    @classmethod
    def get_one_by_email(cls, email):
        query = '''
                SELECT * FROM users 
                WHERE email = %(email)s
                '''
        data = {'email': email}
        results = connectToMySQL('log_in_db').query_db(query, data)
        if len(results) == 0:
            return False
        else: 
            return cls(results[0])

    @classmethod
    def get_one(cls, user_id):
        query = '''
                SELECT * FROM users 
                WHERE id = %(id)s
                '''
        data = {'id': user_id}
        results = connectToMySQL('log_in_db').query_db(query, data)
        return cls(results[0])


    @staticmethod
    def validate(form):

        is_valid = True

        if len(form['first_name']) < 2:
            flash('Name is too short!')
            is_valid = False

        if len(form['last_name']) < 2:
            flash('Last name is too short!')
            is_valid = False

        if len(form['email']) < 2:
            flash('Email is too short!')
            is_valid = False

        if len(form['password']) < 2:
            flash('Password is too short!')
            is_valid = False

        if not EMAIL_REGEX.match(form['email']):
            flash('Invalid email address')
            is_valid = False

        return is_valid




    # @classmethod
    # def register_user(cls, form_data):

    #     hashed_password = bcrypt.generate_password_hash(form_data['password'])
    #     print(hashed_password)

    #     user_data = {
    #         **form_data,
    #         'password' : hashed_password,
    #     }

    #     query = '''
    #         INSERT INTO users (name, email, password)
    #         VALUES (%(name)s, %(email)s, %(password)s
    #     '''
    #     new_user_id = connectToMySQL('log_in_db').query_db(query, user_data)



    # @classmethod
    # def read(cls):
        
    #     query = "SELECT * FROM users"
    #     results = connectToMySQL('log_in_db').query_db(query)

    #     all_users = []

    #     for row in results:
    #         new_user = cls(row)
    #         all_users.append(new_user)

    #     return all_users




    # @classmethod
    # def update(cls,data):
    #     query = '''
    #             UPDATE users 
    #             SET first_name=%(first_name)s,last_name=%(last_name)s,
    #             email=%(email)s, password=%(password)s, 
    #             confirm_password=%(confirm_password)s  WHERE id = %(id)s;
    #             '''
    #     return connectToMySQL('log_in_db').query_db(query,data)
    #     return results



    # @classmethod
    # def delete(cls, user_id):
    #     query = '''
    #             DELETE FROM users WHERE id = %(id)s;
    #             '''
    #     results = connectToMySQL('users_db').query_db(query, {'id': user_id})
    #     return results




    # @classmethod
    # def get_one_with_ninjas(cls, dojo_id):
    #     query = '''
    #             SELECT * FROM dojos LEFT JOIN 
    #             ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id
    #             = %(id)s; '''

    #     data = {'id':dojo_id}

    #     results = connectToMySQL('dojoninjas_db').query_db(query, data)
    #     print(results)

    #     dojo = cls(results[0])
    #     for row_from_db in results:

    #         ninja_data = {
    #             'id' : row_from_db['ninjas.id'],
    #             'first_name' : row_from_db['first_name'],
    #             'last_name' : row_from_db['last_name'],
    #             'age' : row_from_db['age'],
    #             'created_at' :row_from_db['ninjas.created_at'],
    #             'updated_at' : row_from_db['ninjas.updated_at']
    #         }
    #         ninja = Ninjas(ninja_data)
    #         dojo.ninjas.append(ninja)
    #     return dojo