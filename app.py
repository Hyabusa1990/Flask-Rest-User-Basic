from flask import Flask
from flask_migrate import Migrate

from config import Config
from extensions import jwt, db
from models.userModel import User
from resources.homeResource import home_api
from resources.tokenResource import token_api
from resources.userResource import user_api

# INIT Flask
app = Flask(__name__)
app.config.from_object(Config)

# ADD SQLAlchemy into Flask
db.init_app(app)
# ADD Migration to Flask
migrate = Migrate(app, db)
# ADD JWT to Flask
jwt.init_app(app)


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
app.register_blueprint(home_api, url_prefix='')  # ADD Home Routes
app.register_blueprint(user_api, url_prefix='/user')  # ADD User Routes
app.register_blueprint(token_api, url_prefix='/token')  # ADD Token Routes

if __name__ == '__main__':
    app.run()
