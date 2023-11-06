#class methods

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninjas

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojoninjas_db').query_db(query)
        print(results)
        all_dojos = []
        for row in results:
            dojo = cls(row)
            all_dojos.append(dojo)
        print(all_dojos)
        return all_dojos

    @classmethod
    def create(cls, data):
        query = '''
                INSERT into dojos (name)
                VALUES (%(name)s)
                '''
        return connectToMySQL('dojoninjas_db').query_db(query, data)

    @classmethod
    def read(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojoninjas_db').query_db(query)
        all_ninjas = []
        for row in results:
            new_ninja = cls(row)
            all_ninjas.append(new_user)
        return all_ninjas

    @classmethod
    def delete(cls, user_id):
        query = '''
                DELETE FROM dojos WHERE id = %(id)s;
                '''
        results = connectToMySQL('dojoninjas_db').query_db(query, {'id': user_id})
        return results

    @classmethod
    def get_one(cls, user_id):
        query = '''
                SELECT * FROM dojos 
                WHERE id = %(id)s
                '''
        data = {'id': user_id}
        results = connectToMySQL('dojoninjas_db').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_one_with_ninjas(cls, dojo_id):
        query = '''
                SELECT * FROM dojos LEFT JOIN 
                ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id
                = %(id)s; '''

        data = {'id':dojo_id}

        results = connectToMySQL('dojoninjas_db').query_db(query, data)
        print(results)

        dojo = cls(results[0])
        for row_from_db in results:

            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' :row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at']
            }
            ninja = Ninjas(ninja_data)
            dojo.ninjas.append(ninja)
        return dojo

