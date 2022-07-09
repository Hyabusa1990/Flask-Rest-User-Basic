from flask import request, Blueprint, jsonify, abort
from flask_jwt_extended import jwt_required, current_user
from http import HTTPStatus
from models.userModel import User

user_api = Blueprint('userResource', __name__)


def check_if_user_exist(user_id):
    if not User.get_by_id(user_id):
        abort(404, message="User {} doesn't exist".format(user_id))


@user_api.route('/', methods=['POST'])
def add_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if User.get_by_username(username=username):
        return jsonify({'message': 'username already in use'}), HTTPStatus.BAD_REQUEST

    user = User(
        Username=username,
        Password=password
    )

    user.save()

    return jsonify({"data": user.data, 'message': 'OK'}), HTTPStatus.CREATED


@user_api.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = User.get_all()
    return jsonify({'data': [user.data for user in users], 'message': 'OK'}), HTTPStatus.OK


@user_api.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    check_if_user_exist(user_id=user_id)
    user = User.get_by_id(user_id=user_id)
    return jsonify({'data': user.data, 'message': 'OK'}), HTTPStatus.OK


@user_api.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    check_if_user_exist(user_id=user_id)

    if current_user.id == user_id:
        user = User.get_by_id(user_id=user_id)
        user.delete()

        return jsonify({'message': 'User {} deleted'.format(user_id)}), HTTPStatus.OK
    else:
        return jsonify({'message': 'Unauthorized'}), HTTPStatus.UNAUTHORIZED


@user_api.route('/<int:user_id>', methods=['PATCH'])
@jwt_required()
def update_user(user_id):
    check_if_user_exist(user_id=user_id)

    if current_user.id == user_id:
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        user = User.get_by_id(user_id=user_id)

        user.Username = username
        user.Password = password

        user.save()

        return jsonify({'data': user.data, 'message': 'OK'}), HTTPStatus.OK
    else:
        return jsonify({'message': 'Unauthorized'}), HTTPStatus.UNAUTHORIZED
