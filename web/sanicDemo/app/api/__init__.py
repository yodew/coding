from sanic import Blueprint
from app.api.demo import demo_bp
from app.api.demo import ws_bp
api_bp = Blueprint.group(demo_bp, url_prefix="/api")
