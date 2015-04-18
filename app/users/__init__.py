__author__ = 'codnee'
from flask.ext.security import Security, SQLAlchemyUserDatastore
from models import User, Role
from app import app, db

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)