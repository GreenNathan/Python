#class methods

# from flask_app.config.mysqlconnection import connectToMySQL

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
        return connectToMySQL('cardealz_db').query_db(query, data)

    @classmethod
    def get_one_by_email(cls, email):
        query = '''
                SELECT * FROM users 
                WHERE email = %(email)s
                '''
        data = {'email': email}
        results = connectToMySQL('cardealz_db').query_db(query, data)
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
        results = connectToMySQL('cardealz_db').query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate(form):

        is_valid = True

        if len(form['first_name']) < 3:
            flash('Name is too short!')
            is_valid = False

        if len(form['last_name']) < 3:
            flash('Last name is too short!')
            is_valid = False

        if len(form['email']) < 2:
            flash('Email is too short!')
            is_valid = False

        if len(form['password']) < 8:
            flash('Password is too short!')
            is_valid = False

        if not EMAIL_REGEX.match(form['email']):
            flash('Invalid email address')
            is_valid = False

        return is_valid

    @classmethod
    def delete(cls, user_id):
        query = '''
                DELETE FROM users WHERE id = %(id)s;
                '''
        results = connectToMySQL('cardealz_db').query_db(query, {'id': user_id})
        return results


























# class Users:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']



    # @classmethod
    # def create(cls, data):
    #     query = '''
    #             INSERT into Users (first_name, last_name, email)
    #             VALUES (%(first_name)s, %(last_name)s, %(email)s)
    #             '''
    #     return connectToMySQL('users_db').query_db(query, data)
        

    # @classmethod
    # def read(cls):
        
    #     query = "SELECT * FROM users"
    #     results = connectToMySQL('users_db').query_db(query)

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
    #             email=%(email)s WHERE id = %(id)s;
    #             '''
    #     return connectToMySQL('users_db').query_db(query,data)
    #     return results

    # @classmethod
    # def delete(cls, user_id):
    #     query = '''
    #             DELETE FROM users WHERE id = %(id)s;
    #             '''
    #     results = connectToMySQL('users_db').query_db(query, {'id': user_id})
    #     return results


    # @classmethod
    # def get_one(cls, user_id):
    #     query = '''
    #             SELECT * FROM users 
    #             WHERE id = %(id)s
    #             '''
    #     data = {'id': user_id}
    #     results = connectToMySQL('users_db').query_db(query, data)
    #     return cls(results[0])