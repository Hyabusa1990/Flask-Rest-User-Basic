from flask import request, jsonify, Blueprint
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, current_user
from models.userModel import User

token_api = Blueprint('tokenResource', __name__)


@token_api.route('/', methods=['POST'])
def get_token():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.login(username=username, password=password)

    if user is None:
        return jsonify({'message': 'login data is incorrect'}), HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=user, fresh=True)
    refresh_token = create_refresh_token(identity=user)

    return jsonify({'message': 'OK', 'data': {'access_token': access_token, 'refresh_token': refresh_token}}), HTTPStatus.OK


@token_api.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def ref_token():
    access_token = create_access_token(identity=current_user, fresh=False)
    return jsonify({'message': 'OK', 'data': {'access_token': access_token}}), HTTPStatus.OK
