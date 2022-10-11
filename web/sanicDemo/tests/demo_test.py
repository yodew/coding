import pytest

from app import my_app


@pytest.fixture
def app():
    return my_app


class TestDemo(object):

    @pytest.mark.asyncio
    async def test_info(self, app):
        request, response = await app.asgi_client.get("/api/demo/info")
        assert request.method.lower() == "get"
        assert response.body == b'{"content":"Sanic Demo"}'
        assert response.status == 200

    @pytest.mark.asyncio
    async def test_info_2(self, app):
        request, response = await app.asgi_client.get("/api/demo/info")
        assert request.method.lower() == "get"
        assert response.body == b'{"content":"Sanic Demo"}'
        assert response.status == 200
