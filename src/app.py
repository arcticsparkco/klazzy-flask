#src/app.py

from flask import Flask
from flask_cors import CORS, cross_origin

import os

from .config import app_config
from .models import db
from .models import bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint
from .views.EventView import event_api as event_blueprint
from .views.DealView import deal_api as deal_blueprint
from .views.PlaceView import place_api as place_blueprint


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  cors = CORS(app)
  app.config['CORS_HEADERS'] = 'Content-Type'

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
  app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')
  app.register_blueprint(event_blueprint, url_prefix='/api/v1/events')
  app.register_blueprint(deal_blueprint, url_prefix='/api/v1/deals')
  app.register_blueprint(place_blueprint, url_prefix='/api/v1/places')

  @app.route('/', methods=['GET'])
  @cross_origin()
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your part 2 endpoint is working'

  return app

