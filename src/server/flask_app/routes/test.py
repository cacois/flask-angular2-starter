from flask import Blueprint, Response, request
from flask_security import auth_token_required
from ..app_utils import html_codes, token_login
import json

test = Blueprint('test', __name__, url_prefix='/api')

@test.route('/getdata', methods=['POST', 'GET'])
@auth_token_required
def get_data():
    """Get dummy data returned from the server."""
    data = {'Heroes': ['Hero1', 'Hero2', 'Hero3']}
    json_response = json.dumps(data)
    return Response(json_response,
                    status=html_codes.HTTP_OK_BASIC,
                    mimetype='application/json')

@test.route('/test', methods=['GET'])
def test_get():
    return Response('test')
