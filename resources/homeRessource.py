from flask_restful import Resource
from http import HTTPStatus


class HomeListResource(Resource):

    def get(self):
        return {"data": "Home"}, HTTPStatus.OK
