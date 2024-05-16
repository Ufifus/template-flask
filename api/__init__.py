from .urls import routes
from .config import Config
from .app import app as child_app

routes(child_app)