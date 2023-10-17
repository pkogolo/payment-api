from flask import Blueprint, request
from .invoices import *
from modules.shared import exceptDefault, exceptSpecific, build_response

invoice_bp = Blueprint('invoices', __name__)

@invoice_bp.route("/")
def home():
    return build_response(200, "it's easier with us")

@invoice_bp.app_errorhandler(404)
def page_not_found(e):
    return exceptSpecific(e)
