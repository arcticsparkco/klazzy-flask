#/src/views/TagView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.TagModel import TagModel, TagSchema

tag_api = Blueprint('tag_api', __name__)
tag_schema = TagSchema()


@tag_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Tag Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = tag_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  tag = TagModel(data)
  tag.save()
  data = tag_schema.dump(tag)
  return custom_response(data, 201)

@tag_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Tags
  """
  tags = TagModel.get_all_tags()
  data = tag_schema.dump(tags, many=True)
  return custom_response(data, 200)

@tag_api.route('/<int:tag_id>', methods=['GET'])
def get_one(tag_id):
  """
  Get A Tag
  """
  tag = TagModel.get_one_tag(tag_id)
  if not tag:
    return custom_response({'error': 'tag not found'}, 404)
  data = tag_schema.dump(tag)
  return custom_response(data, 200)

@tag_api.route('/<int:tag_id>', methods=['PUT'])
@Auth.auth_required
def update(tag_id):
  """
  Update A Tag
  """
  req_data = request.get_json()
  tag = TagModel.get_one_tag(tag_id)
  if not tag:
    return custom_response({'error': 'tag not found'}, 404)
  data = tag_schema.dump(tag)
  # if data.get('owner_id') != g.user.get('id'):
  #   return custom_response({'error': 'permission denied'}, 400)
  
  data, error = tag_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  tag.update(data)
  
  data = tag_schema.dump(tag)
  return custom_response(data, 200)

@tag_api.route('/<int:tag_id>', methods=['DELETE'])
@Auth.auth_required
def delete(tag_id):
  """
  Delete A Tag
  """
  tag = TagModel.get_one_tag(tag_id)
  if not tag:
    return custom_response({'error': 'tag not found'}, 404)
  data = tag_schema.dump(tag)
  # if data.get('owner_id') != g.user.get('id'):
  #   return custom_response({'error': 'permission denied'}, 400)

  tag.delete()
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

