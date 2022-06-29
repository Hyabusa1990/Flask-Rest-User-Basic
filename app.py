from flask import Flask
from config import Config
from flask_restful import Api
from flask_migrate import Migrate
from extensions import jwt, db

from routes.homeRoutes import homeRoutes
from routes.userRoutes import userRoutes

# INIT Flask
app = Flask(__name__)
app.config.from_object(Config)

# ADD SQLAlchemy into Flask
db.init_app(app)
# ADD Migration to Flask
migrate = Migrate(app, db)
# ADD JWT to Flask
jwt.init_app(app)

# INIT Flask Restful API
api = Api(app)

# ADD Routes
homeRoutes(api, '/')  # Home Routes
userRoutes(api, '/user')  # User Routes

if __name__ == '__main__':
    app.run()
