Development
python main.py

Production
gunicorn -w 4 --bind=127.0.0.1 -b 8080 'wsgi:create_app'