from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from resources.item import ItemList, Item

app = Flask(__name__)
app.secret_key = "MarvelBestSecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authenticate, identity)
api = Api(app)

@app.route('/')
def home():
    return redirect("https://documenter.getpostman.com/view/11851415/TVCZaBDJ")

api.add_resource(Item, '/products/<string:name>')
api.add_resource(ItemList, '/products')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port = 5050, debug = True)