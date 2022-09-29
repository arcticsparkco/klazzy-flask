#/src/views/EventView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.EventModel import EventModel, EventSchema

event_api = Blueprint('event_api', __name__)
event_schema = EventSchema()


@event_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Event Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = event_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  event = EventModel(data)
  event.save()
  data = event_schema.dump(event)
  return custom_response(data, 201)

@event_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Events
  """
  events = EventModel.get_all_events()
  data = event_schema.dump(events, many=True)
  return custom_response(data, 200)

@event_api.route('/<int:event_id>', methods=['GET'])
def get_one(event_id):
  """
  Get A Event
  """
  event = EventModel.get_one_event(event_id)
  if not event:
    return custom_response({'error': 'event not found'}, 404)
  data = event_schema.dump(event)
  return custom_response(data, 200)

@event_api.route('/<int:event_id>', methods=['PUT'])
@Auth.auth_required
def update(event_id):
  """
  Update A Event
  """
  req_data = request.get_json()
  event = EventModel.get_one_event(event_id)
  if not event:
    return custom_response({'error': 'event not found'}, 404)
  data = event_schema.dump(event)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = event_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  event.update(data)
  
  data = event_schema.dump(event)
  return custom_response(data, 200)

@event_api.route('/<int:event_id>', methods=['DELETE'])
@Auth.auth_required
def delete(event_id):
  """
  Delete A Event
  """
  event = EventModel.get_one_event(event_id)
  if not event:
    return custom_response({'error': 'event not found'}, 404)
  data = event_schema.dump(event)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  event.delete()
  return custom_response({'message': 'deleted'}, 204)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

