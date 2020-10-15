#!/usr/bin/env python
from server import application, db
from flask_script import Manager, prompt_bool

from models import User

manager = Manager(application)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="test",email="test@example.com",password="test"))
    db.session.add(User(username="test2",email="test2@example.com",password="test2"))
    db.session.commit()
    print("Initialized the database")

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()
        print("Dropped the database")

if __name__ == '__main__':
    manager.run()
