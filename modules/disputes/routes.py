from flask import Blueprint, request
from .disputes import *
from modules.shared import exceptDefault, exceptSpecific, build_response

disputes_bp = Blueprint('disputes', __name__)

@disputes_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@disputes_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)