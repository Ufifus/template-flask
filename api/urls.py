from flask import jsonify, request

from .views import *


def routes(app):
    @app.route('/', methods=['GET'])
    def index_route():
        return index(request)