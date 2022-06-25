from flask import Flask
from config import Config
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from routes.helloWorldRoute import helloWorldRoutes

# INIT Flask
app = Flask(__name__)
app.config.from_object(Config)

# INIT SQLAlchemy + JWT
db = SQLAlchemy()
jwt = JWTManager()

# ADD SQLAlchemy into Flask
db.init_app(app)
# ADD Migration to Flask
migrate = Migrate(app, db)
# ADD JWT to Flask
jwt.init_app(app)

# INIT Flask Restful API
api = Api(app)

# ADD HelloWorld Routes
helloWorldRoutes(api, "/")

if __name__ == '__main__':
    app.run()
