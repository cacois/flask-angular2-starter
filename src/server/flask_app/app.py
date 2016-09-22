"""Entry point for the server application."""

import json
import logging

from flask import Response, request
from flask_security import auth_token_required, utils
from gevent.wsgi import WSGIServer

from .app_utils import html_codes, token_login
from .config import app, configure_app, init_db

logger = logging.getLogger(__name__)


@app.route("/api/logoutuser", methods=['POST'])
@auth_token_required
def logout():
    """Logout the currently logged in user."""
    logger.info('Logged out user !!')
    utils.logout_user()
    return 'logged out successfully', 200


@app.route('/api/loginuser', methods=['POST'])
def login():
    """View function for login view."""
    logger.info('Logged in user')
    return token_login.login_with_token(request, app)


@app.route('/api/getdata', methods=['GET'])
@auth_token_required
def get_data():
    """Get dummy data returned from the server."""
    data = {'Heroes': ['Hero1', 'Hero2', 'Hero3']}
    json_response = json.dumps(data)
    return Response(json_response,
                    status=html_codes.HTTP_OK_BASIC,
                    mimetype='application/json')

@app.route('/api/test', methods=['GET'])
def test():
    return Response('wee')

def run():
    """Main entry point of the app."""
    try:
        configure_app()
        app.run('0.0.0.0', 8081)
        init_db()

    except Exception as exc:
        logger.error(exc.message)
    finally:
        # get last entry and insert build appended if not completed
        # Do something here
        pass
