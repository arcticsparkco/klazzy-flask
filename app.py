# /run.py
import os
# from dotenv import load_dotenv, find_dotenv

from src.app import create_app

# load_dotenv(find_dotenv())

env_name = os.getenv('FLASK_ENV')
print("env_name" + env_name)

app = create_app(env_name)

if __name__ == '__main__':
  port = os.getenv('5000')
  # run app
  app.run(host='0.0.0.0', port=port)
