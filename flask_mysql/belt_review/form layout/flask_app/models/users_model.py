#class methods

from flask_app.config.mysqlconnection import connectToMySQL



class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def create(cls, data):
        query = '''
                INSERT into Users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s)
                '''
        return connectToMySQL('recipe_db').query_db(query, data)
        

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