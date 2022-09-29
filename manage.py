import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db

# env_name = os.getenv('FLASK_ENV' or 'default') 

app = create_app(os.getenv('FLASK_CONFIG') or 'application')

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
