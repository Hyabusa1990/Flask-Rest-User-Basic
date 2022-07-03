from flask import request
from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.userModel import User


class TokenResource(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.login(username=username, password=password)

        if user is None:
            return {'message': 'login data is incorrect'}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user, fresh=True)
        refresh_token = create_refresh_token(identity=user)

        return {'access_token': access_token, 'refresh_token': refresh_token}, HTTPStatus.OK


class RefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': access_token}, HTTPStatus.OK
