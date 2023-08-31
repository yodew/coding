from sanic import Blueprint
from app.api.demo.info import info_bp
from app.api.demo.hello import hello_bp, hello_bp2
from app.api.demo.feed import ws_bp
from app.api.demo.view import sample_view_bp

demo_bp = Blueprint.group(info_bp, hello_bp, hello_bp2, sample_view_bp, url_prefix="/demo")
