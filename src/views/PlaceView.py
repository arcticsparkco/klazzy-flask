#/src/views/PlaceView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.PlaceModel import PlaceModel, PlaceSchema

place_api = Blueprint('place_api', __name__)
place_schema = PlaceSchema()


@place_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Place Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = place_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  place = PlaceModel(data)
  place.save()
  data = place_schema.dump(place)
  return custom_response(data, 201)

@place_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Places
  """
  places = PlaceModel.get_all_places()
  data = place_schema.dump(places, many=True)
  return custom_response(data, 200)

@place_api.route('/<int:place_id>', methods=['GET'])
def get_one(place_id):
  """
  Get A Place
  """
  place = PlaceModel.get_one_place(place_id)
  if not place:
    return custom_response({'error': 'place not found'}, 404)
  data = place_schema.dump(place)
  return custom_response(data, 200)

@place_api.route('/<int:place_id>', methods=['PUT'])
@Auth.auth_required
def update(place_id):
  """
  Update A Place
  """
  req_data = request.get_json()
  place = PlaceModel.get_one_place(place_id)
  if not place:
    return custom_response({'error': 'place not found'}, 404)
  data = place_schema.dump(place)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = place_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  place.update(data)
  
  data = place_schema.dump(place)
  return custom_response(data, 200)

@place_api.route('/<int:place_id>', methods=['DELETE'])
@Auth.auth_required
def delete(place_id):
  """
  Delete A Place
  """
  place = PlaceModel.get_one_place(place_id)
  if not place:
    return custom_response({'error': 'place not found'}, 404)
  data = place_schema.dump(place)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  place.delete()
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

