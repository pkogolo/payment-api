from flask import Blueprint, request
from .events import *
from modules.shared import exceptDefault, exceptSpecific, build_response

events_bp = Blueprint('events', __name__)

@events_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@events_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)