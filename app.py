# # /run.py
# import os
# # from dotenv import load_dotenv, find_dotenv

# from src.app import create_app

# # load_dotenv(find_dotenv())

# env_name = os.getenv('FLASK_ENV')
# print("env_name" + env_name)

# app = create_app(env_name)

# if __name__ == '__main__':
#   port = os.getenv('5000')
#   # run app
#   application.debug = True
#   app.run(host='0.0.0.0', port=port)



from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
       app.run()