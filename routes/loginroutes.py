from flask import Blueprint
from controllers.logincontroller import index, login, signin, logout

login_bp = Blueprint('login', __name__)

login_bp.add_url_rule('/', view_func=index)
login_bp.add_url_rule('/login', methods=['GET', 'POST'], view_func=login)
login_bp.add_url_rule('/signin', methods=['GET', 'POST'], view_func=signin)
login_bp.add_url_rule('/logout', view_func=logout)