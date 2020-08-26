from db import db

class ItemModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    price = db.Column(db.Float(precision=2))

    def __init__(self, _id, name, price):
        self.id = ItemModel.id_identificator(_id)
        self.name = name
        self.price = price


    def json(self):
        return {"ID": self.id, "name": self.name, "price": self.price}


    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def id_identificator(cls, _id):
        item = ItemModel.get_db()
        if item:
            for person in item:
                if _id == person.id:
                    _id += 1
            return _id
        else:
            return _id

    @classmethod
    def get_db(cls):
        persons = cls.query.filter_by().all()
        return persons

    @classmethod
    def get_db(cls):
        items = cls.query.filter_by().all()
        return items
