from flask_restful import Api
from resources.userResource import UserListResource, UserResource


def userRoutes(api: Api, baseurl: str):
    api.add_resource(UserListResource, baseurl)
    api.add_resource(UserResource, baseurl + '/<user_id>')
