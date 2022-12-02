from sanic import Blueprint
from sanic.response import json

info_bp = Blueprint("info")


@info_bp.get("/info")
async def info(request):
    return json({"content": "Sanic Demo"})
