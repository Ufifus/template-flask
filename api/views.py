import logging

import psycopg2
import psycopg2.extras
from flask import jsonify

from utils import jwt_decorator, db_decorator, CustomError

logger = logging.getLogger(__name__)


@jwt_decorator
@db_decorator
def index(conn, request):
    """
    Пример написания сетевой функции
    @jwt_decorator # декоратор для авторизации пользователя
    @db_decorator # декоратор предоставляющий доступ к бд (можно от него отказаться но для единого стиля и упрощения не стоит)
    def <view_func>(conn, request):   # название функции и переменные, первые две переменные всего conn (соедиение с базой), request (параметры запроса)
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:  # Открываем курсор для операций в бд
            ... # операции
            # если надо вызывать исключения то вызываются они только методом raise CustomError(message: str, code : int)
            # (в декораторе прописан rollback так что не надо его вызывать напрямую)
            conn.commit() # Опциональное поле для сохранения измений в бд
        return jsonify(...), <status_code> # Возвращаем json и статус ошибки
    """
    logger.debug('Handling index request: %s', request.path)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT count(*) FROM filler_xml")
        count = cur.fetchone()[0]
        if count < 1000:
            logger.warning('Data count below threshold: %d', count)
            raise CustomError('Error view checking', 404)
    return jsonify({'working': True}), 200
