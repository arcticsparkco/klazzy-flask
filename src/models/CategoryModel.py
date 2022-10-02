# src/models/CategoryModel.py
from . import db
import datetime
from marshmallow import fields, Schema

class CategoryModel(db.Model):
  """
  Category Model
  """

  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)

  def __init__(self, data):
    self.name = data.get('name')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_categories():
    return CategoryModel.query.all()
  
  @staticmethod
  def get_one_category(id):
    return CategoryModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class CategorySchema(Schema):
  """
  Category Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)


