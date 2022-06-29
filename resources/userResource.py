from flask import request
from flask_restful import Resource, abort
from http import HTTPStatus
from models.userModel import User
import json


def check_if_user_exist(user_id):
    if not User.get_by_id(user_id):
        abort(404, message="User {} doesn't exist".format(user_id))


class UserListResource(Resource):

    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if User.get_by_username(username=username):
            return {'message': 'username already in use'}, HTTPStatus.BAD_REQUEST

        hashed_password = User.hash_password(password)

        user = User(
            username=username,
            password=hashed_password
        )

        user.save()

        return {"data": user.data, 'message': ''}, HTTPStatus.CREATED

    def get(self):
        users = User.get_all()
        return {'data': [user.data for user in users], 'message': 'OK'}, HTTPStatus.OK


class UserResource(Resource):

    def get(self, user_id):
        check_if_user_exist(user_id=user_id)
        return User.get_by_id(user_id=user_id)

    def delete(self, user_id):
        check_if_user_exist(user_id=user_id)

        user = User.get_by_id(user_id=user_id)
        user.delete()

        return {'message': 'User {} deleted'.format(user_id)}, HTTPStatus.OK

    def put(self, user_id):
        check_if_user_exist(user_id=user_id)
        data = request.get_json()

        username = data.get('username')
        password = User.hash_password(data.get('password'))

        user = User.get_by_id(user_id=user_id)

        user.data.username = username
        user.data.password = password

        user.save()

        return {'data': user.data, 'message': 'OK'}, HTTPStatus.OK