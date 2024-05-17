from flask import request

from .views import *


def routes(app):
    """
    Делаем связь наших функций с проектом
    делается через декоратор как в примере ниже,

    @app.route('/<url>', methods=["GET", "POST", "PUT", "DELETE"]) # опционально прописываются методы REST, но мы будем делать только по одному методу в ф-и
    def <view_func>_route(): # храним название функции из .views с названием <view_func> и припиской _route чтобы сохранить уникальность
        return <view_func>() # вызываем функцию из .views с названием <view_func>
    """

    @app.route('/', methods=['GET'])
    def index_route():
        return index(request)
