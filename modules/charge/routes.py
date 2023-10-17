from flask import Blueprint, request
from .charge import *
from modules.shared import exceptDefault, exceptSpecific, build_response

charge_bp = Blueprint('charge', __name__)

@charge_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@charge_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)
