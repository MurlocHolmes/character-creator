from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = None

class Model(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__


def connect(app):
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/app/data/test.db'
    db = SQLAlchemy(app)


def connect_collection(collection):
    return db.universe[collection]


def format_name(name):
    return ''.join(e.lower() for e in name if e.isalnum())


def check_universe_exists(universe):
    return False


def add_record(model, data):
    model.init(data)
    db.session.add(model)
    db.session.commit()
    return model


def update_record(model_class, data):
    model = model_class.query.filter_by(name=data['name']).first()
    model.init(data)
    db.session.commit()
    return model
