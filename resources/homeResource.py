from flask import Blueprint, jsonify
from http import HTTPStatus

home_api = Blueprint('homeResource', __name__)


@home_api.route('/', methods=['GET'])
def home():
    return jsonify({"data": "Home"}), HTTPStatus.OK
