from flask import Blueprint

web_bp = Blueprint('web', __name__)

from choujiang.blueprints.web import  weixin
