from flask import Blueprint, request
from .accounts import *
from modules.shared import exceptDefault, exceptSpecific, build_response

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@accounts_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)