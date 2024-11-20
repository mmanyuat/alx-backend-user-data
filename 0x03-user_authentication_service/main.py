#!/usr/bin/env python3
"""
Main file
"""
import logging
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from db import DB

# Suppress SQLAlchemy debug logs
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)

my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")

