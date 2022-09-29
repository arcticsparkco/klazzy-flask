#/src/views/DealView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.DealModel import DealModel, DealSchema

deal_api = Blueprint('deal_api', __name__)
deal_schema = DealSchema()


@deal_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Deal Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = deal_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  deal = DealModel(data)
  deal.save()
  data = deal_schema.dump(deal)
  return custom_response(data, 201)

@deal_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Deals
  """
  deals = DealModel.get_all_deals()
  data = deal_schema.dump(deals, many=True)
  return custom_response(data, 200)

@deal_api.route('/<int:deal_id>', methods=['GET'])
def get_one(deal_id):
  """
  Get A Deal
  """
  deal = DealModel.get_one_deal(deal_id)
  if not deal:
    return custom_response({'error': 'deal not found'}, 404)
  data = deal_schema.dump(deal)
  return custom_response(data, 200)

@deal_api.route('/<int:deal_id>', methods=['PUT'])
@Auth.auth_required
def update(deal_id):
  """
  Update A Deal
  """
  req_data = request.get_json()
  deal = DealModel.get_one_deal(deal_id)
  if not deal:
    return custom_response({'error': 'deal not found'}, 404)
  data = deal_schema.dump(deal)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = deal_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  deal.update(data)
  
  data = deal_schema.dump(deal)
  return custom_response(data, 200)

@deal_api.route('/<int:deal_id>', methods=['DELETE'])
@Auth.auth_required
def delete(deal_id):
  """
  Delete A Deal
  """
  deal = DealModel.get_one_deal(deal_id)
  if not deal:
    return custom_response({'error': 'deal not found'}, 404)
  data = deal_schema.dump(deal)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  deal.delete()
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

