# src/models/EventModel.py
from . import db
import datetime
from marshmallow import fields, Schema

class EventModel(db.Model):
  """
  Event Model
  """

  __tablename__ = 'events'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.Text, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.name = data.get('name')
    self.description = data.get('description')
    self.owner_id = data.get('owner_id')
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
  def get_all_events():
    return EventModel.query.all()
  
  @staticmethod
  def get_one_event(id):
    return EventModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class EventSchema(Schema):
  """
  Event Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  description = fields.Str(required=True)
  owner_id = fields.Int(required=False)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
