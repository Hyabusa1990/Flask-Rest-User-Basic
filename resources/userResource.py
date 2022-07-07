from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource, abort
from http import HTTPStatus
from models.userModel import User


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

        user = User(
            Username=username,
            Password=password
        )

        user.save()

        return {"data": user.data, 'message': 'OK'}, HTTPStatus.CREATED

    @jwt_required()
    def get(self):
        users = User.get_all()
        return {'data': [user.data for user in users], 'message': 'OK'}, HTTPStatus.OK


class UserResource(Resource):

    @jwt_required()
    def get(self, user_id):
        check_if_user_exist(user_id=user_id)
        return User.get_by_id(user_id=user_id)

    @jwt_required()
    def delete(self, user_id):
        check_if_user_exist(user_id=user_id)

        if current_user.id == user_id:
            user = User.get_by_id(user_id=user_id)
            user.delete()

            return {'message': 'User {} deleted'.format(user_id)}, HTTPStatus.OK
        else:
            return {'message': 'Unauthorized'}, HTTPStatus.UNAUTHORIZED

    @jwt_required()
    def put(self, user_id):
        check_if_user_exist(user_id=user_id)

        if current_user.id == user_id:
            data = request.get_json()

            username = data.get('username')
            password = data.get('password')

            user = User.get_by_id(user_id=user_id)

            user.Username = username
            user.Password = password

            user.save()

            return {'data': user.data, 'message': 'OK'}, HTTPStatus.OK
        else:
            return {'message': 'Unauthorized'}, HTTPStatus.UNAUTHORIZED
