from flask import Blueprint, request
from .pay import *
from modules.shared import exceptDefault, exceptSpecific, build_response

pay_bp = Blueprint('payments', __name__)

@pay_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@pay_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)

@pay_bp.route("/payout")
def payout():

    return paysout("samson", "garose")