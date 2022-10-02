#src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()

from .BlogpostModel import BlogpostModel, BlogpostSchema
from .UserModel import UserModel, UserSchema
from .DealModel import DealSchema, DealModel
from .EventModel import EventSchema, EventModel
from .TagModel import TagSchema, TagModel
from .CategoryModel import CategorySchema, CategoryModel