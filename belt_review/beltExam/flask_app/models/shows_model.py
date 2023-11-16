
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import Users
from flask import flash


class Shows:
    def __init__(self, data):
        self.id = data['id']
        self.title= data['title']
        self.network = data ['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def createshow(cls, data):
        query = '''
                INSERT into shows (title, network, release_date, description, users_id)
                VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(users_id)s)
                '''
        return connectToMySQL('tvshows_db').query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        
        query = '''SELECT * FROM shows JOIN users ON 
        shows.users_id = users.id;'''

        results = connectToMySQL('tvshows_db').query_db(query)
        print(results)
        all_shows = []

        for row in results:
            new_show = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'pw_hash':row['pw_hash'],
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at']
            }
            new_show.user= Users(user_data)
            all_shows.append(new_show)

        return all_shows

    @classmethod
    def update(cls,data):
        query = '''
                UPDATE shows 
                SET title= %(title)s, network= %(network)s, release_date=%(release_date)s,
                description= %(description)s WHERE id = %(id)s;
                '''
        return connectToMySQL('tvshows_db').query_db(query,data)
        return results


    @classmethod
    def get_one(cls, show_id):
        query = '''SELECT * FROM shows JOIN users ON 
        shows.users_id = users.id WHERE shows.id = %(id)s;'''
        data = {'id': show_id}
        results = connectToMySQL('tvshows_db').query_db(query, data)
        
        print(results)

        new_show = cls(results[0])
        user_data = {
            'id': results[0]['users.id'],
            'first_name':results[0]['first_name'],
            'last_name':results[0]['last_name'],
            'email':results[0]['email'],
            'pw_hash':results[0]['pw_hash'],
            'created_at':results[0]['users.created_at'],
            'updated_at':results[0]['users.updated_at']
        }
        new_show.user= Users(user_data)
        
        return new_show

    @staticmethod
    def validated(form):
        
        is_valid = True

        if len(form['title']) < 3:
            flash('Must input cooler Title!')
            is_valid = False
            
        if len(form['network']) < 3:
            flash('Must input cool Network!')
            is_valid = False

        if len(form['description']) < 3:
            flash('Must input better description!')
            is_valid = False

        return is_valid

    @classmethod
    def delete(cls, show_id):
        query = '''
                DELETE FROM shows WHERE id = %(id)s;
                '''
        results = connectToMySQL('tvshows_db').query_db(query, {'id': show_id})
        return results