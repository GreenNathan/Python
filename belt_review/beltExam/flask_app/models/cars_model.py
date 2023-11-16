
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import Users


class Cars:
    def __init__(self, data):
        self.id = data['id']
        self.model= data['model']
        self.price = data ['price']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def createcar(cls, data):
        query = '''
                INSERT into cars (model, year, make, price, description, users_id)
                VALUES (%(model)s, %(year)s, %(make)s, %(price)s,%(description)s, %(users_id)s)
                '''
        return connectToMySQL('cardealz_db').query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        
        query = '''SELECT * FROM cars JOIN users ON 
        cars.users_id = users.id;'''

        results = connectToMySQL('cardealz_db').query_db(query)
        print(results)
        all_cars = []

        for row in results:
            new_car = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'pw_hash':row['pw_hash'],
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at']
            }
            new_car.user= Users(user_data)
            all_cars.append(new_car)

        return all_cars

    @classmethod
    def update(cls,data):
        query = '''
                UPDATE cars 
                SET model= %(model)s, year= %(year)s,
                description= %(description)s WHERE id = %(id)s;
                '''
        return connectToMySQL('cardealz_db').query_db(query,data)
        return results


    @classmethod
    def get_one(cls, car_id):
        query = '''SELECT * FROM cars JOIN users ON 
        cars.users_id = users.id WHERE cars.id = %(id)s;'''
        data = {'id': car_id}
        results = connectToMySQL('cardealz_db').query_db(query, data)
        
        print(results)

        new_car = cls(results[0])
        user_data = {
            'id': results[0]['users.id'],
            'first_name':results[0]['first_name'],
            'last_name':results[0]['last_name'],
            'email':results[0]['email'],
            'pw_hash':results[0]['pw_hash'],
            'created_at':results[0]['users.created_at'],
            'updated_at':results[0]['users.updated_at']
        }
        new_car.user= Users(user_data)
        
        return new_car

    @classmethod
    def delete(cls, car_id):
        query = '''
                DELETE FROM cars WHERE id = %(id)s;
                '''
        results = connectToMySQL('cardealz_db').query_db(query, {'id': car_id})
        return results