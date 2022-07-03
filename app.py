from flask import Flask
from config import Config
from flask_restful import Api
from flask_migrate import Migrate
from extensions import jwt, db
from models.userModel import User

from routes.homeRoutes import homeRoutes
from routes.userRoutes import userRoutes
from routes.tokenRoutes import tokenRoutes

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


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


# ADD Routes
homeRoutes(api, '/')  # Home Routes
userRoutes(api, '/user')  # User Routes
tokenRoutes(api, '/token')  # Token Routes

if __name__ == '__main__':
    app.run()
