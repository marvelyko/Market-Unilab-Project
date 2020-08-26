from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

import sqlite3


class Item(Resource):
    TABLE_NAME = 'store'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="გთხოვთ შეიყვანოთ პროდუქტის ღირებულება")



    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': f'მონაცემი {name} ბაზაში ვერ მოიძებნა'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'მონაცემი {name} ბაზაში უკვე არსებობს'}, 400

        data = self.parser.parse_args()

        item = ItemModel(1, name, data['price'])

        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"{e}"}
        else:
            return item.json()

    def put(self, name):

        item = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()

        if item:
            item.price=data['price']
        else:
            item = ItemModel(1, name, data['price'])

        item.save_to_db()

        return {'item': item.json()}

    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()
            return {'message': 'მონაცემი წარმატებით წაიშალა.'}
        else:
            return {'message': 'მონაცემი ბაზაში ვერ მოიძებნა.'}


# class ItemList(Resource):
#     @jwt_required()
#     def get(self):
#         conn = sqlite3.connect('data.db')
#         cursor = conn.cursor()
#
#         results = cursor.execute("SELECT * FROM store ORDER BY ღირებულება")
#
#         items = []
#
#         for item in results:
#             items.append({
#                 "დასახელება": item[0],
#                 "ღირებულება": item[1],
#                 "რაოდენობა": item[2]
#             })
#
#         conn.close()
#         print(items)
#
#         return {"მენიუ": items}

class ItemList(Resource):
    @jwt_required()
    def get(self):

        items = ItemModel.get_db()
        _items = []
        for item in items:
            _items.append(item.json())
        return {"message": _items}