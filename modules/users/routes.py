from flask import Blueprint, request
from modules.shared import exceptDefault, exceptSpecific, build_response
users_bp = Blueprint('users', __name__)

@users_bp.route("/")
def home():
    return  build_response(200, "it's easier with us")

@users_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)



@users_bp.route("/signup")
def signup():
    try:
        return build_response(200, "it's easier with us")
    except Exception as e:
        return exceptSpecific(e, statuscode=500, status="try again")