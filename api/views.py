import psycopg2

from flask import jsonify
from utils import jwt_decorator, db_decorator, CustomError, logger


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
    print(request)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        query = "SET SCHEMA 'ml_main'; SELECT count(*) FROM V_REQUESTLISTFULL"
        logger.error(query)
        cur.execute(query)
        count = cur.fetchone()[0]
        if count < 1000:
            raise CustomError('Error view cheking', 404)
    return jsonify({'working': True}), 200
