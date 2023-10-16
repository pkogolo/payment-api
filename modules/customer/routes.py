from flask import Blueprint, request
from .customer import *
from modules.shared import exceptDefault, exceptSpecific, build_response

customer_bp = Blueprint('customer', __name__)

@customer_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@customer_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)