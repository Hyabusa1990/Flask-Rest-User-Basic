from flask_restful import Resource
from http import HTTPStatus


class HelloWorldListResource(Resource):

    def get(self):
        return {"message": "Hello World"}, HTTPStatus.OK
