# src/models/DealModel.py
from . import db
import datetime
from marshmallow import fields, Schema
from .CategoryModel import CategorySchema
from .TagModel import TagSchema, TagModel
from .CategoryModel import CategorySchema, CategoryModel


deal_tag = db.Table('deal_tag',
                    db.Column('deal_id', db.Integer, db.ForeignKey('deals.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                    )

deal_category = db.Table('deal_category',
                    db.Column('deal_id', db.Integer, db.ForeignKey('deals.id')),
                    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
                    )


class DealModel(db.Model):
  """
  Deal Model
  """

  __tablename__ = 'deals'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.Text, nullable=False)
  url = db.Column(db.Text, nullable=False)
  img = db.Column(db.Text, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  valid_until = db.Column(db.DateTime)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)
  categories = db.relationship('CategoryModel', secondary=deal_category, backref='deals', lazy=True)
  tags = db.relationship('TagModel', secondary=deal_tag, backref='deals', lazy=True)

  def __init__(self, data):
    self.name = data.get('name')
    self.description = data.get('description')
    self.owner_id = data.get('owner_id')
    self.url = data.get('url')
    self.img = data.get('img')
    self.valid_until = datetime.datetime.utcnow()
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_deals():
    return DealModel.query.all()
  
  @staticmethod
  def get_one_deal(id):
    return DealModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class DealSchema(Schema):
  """
  Deal Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  description = fields.Str(required=True)
  # owner_id = fields.Int(required=False)
  url = fields.Str(required=False)
  img = fields.Str(required=False)
  valid_until = fields.DateTime(dump_only=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  deal_creator = fields.Nested("UserSchema", only=('email', 'name'))
  categories = fields.Nested("CategorySchema")
  tags = fields.Nested("TagSchema")
