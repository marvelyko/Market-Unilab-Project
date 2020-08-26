#damatebit shevqmna momxmareblis avtorizaciistvis POST DELETE

from flask_restful import Resource, reqparse
from models.user import UserModel



class User(Resource):
    TABLE_NAME = 'users'
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ მომხმარებლის სახელი")


    def post(self, name):
        if UserModel.find_by_name(name):
            return {'message': f'მონაცემი {name} ბაზაში უკვე არსებობს'}, 400

        data = self.parser.parse_args()

        account = {'დასახელება': name, 'password': data["password"]}
        try:
            self.insert(account)
        except Exception as e:
            return {"message": f"{e}"}
        else:
            return account


    def delete(self, name):
        if UserModel.find_by_name(name):
            try:
                UserModel.delete(name)
            except Exception as e:
                print(e)
                return {'message': 'მოთხოვნის დამუშავებისას დაფიქსირდა შეცდომა.'}
            else:
                return {'message': 'მონაცემი წარმატებით წაიშალა.'}
        else:
            return {'message': 'მონაცემი ბაზაში ვერ მოიძებნა.'}

