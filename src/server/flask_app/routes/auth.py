from flask import Blueprint, Response, request
from flask_security import auth_token_required, utils
from ..app_utils import html_codes, token_login
import logging

auth = Blueprint('auth', __name__, url_prefix='/api')
logger = logging.getLogger(__name__)

@auth.route("/logoutuser", methods=['POST'])
@auth_token_required
def logout():
    """Logout the currently logged in user."""
    logger.info('Logged out user !!')
    utils.logout_user()
    return 'logged out successfully', 200


@auth.route('/loginuser', methods=['POST'])
def login():
    """View function for login view."""
    from ..app import app
    logger.info('Logged in user')
    return token_login.login_with_token(request, app)
