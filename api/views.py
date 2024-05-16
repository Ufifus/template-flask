import psycopg2

from flask import jsonify
from utils import jwt_decorator, db_decorator


@jwt_decorator
@db_decorator
def index(conn, request):
    print(request)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT count(*) FROM filler_xml")
        print(cur.fetchone())
    return jsonify({'working': True}), 200
