from arq import create_pool
from arq.connections import RedisSettings, ArqRedis
from arq.worker import Worker
from sanic import Sanic

__version__ = "0.1.0"

from sanic.log import logger


class SanicArq:
    """
        Arq Class for Sanic
    """

    app: Sanic
    redis_url: str
    config_name: str

    def __init__(self, app: Sanic = None):
        """
            init method of class
        """

        self.__version__ = __version__
        self.app: Sanic = app
        self.arq_redis: ArqRedis | None = None
        self.arq_worker: Worker | None = None
        if app:
            self.init_app(app=app)

    def version(self):
        """
            dummy function to pass pylint
        """

        return self.__version__

    def init_app(self, app: Sanic, config_name: str = "REDIS_P_B"):
        """
            init_app for Sanic
        """

        self.app = app
        if config_name:
            self.config_name = config_name

        @app.listener('before_server_start')
        async def aio_redis_configure(_app: Sanic, _loop):
            self._redis_url = _app.config.get(self.config_name)
            if not self._redis_url:
                raise ValueError(
                    f"You must specify a redis_url or set the "
                    f"{config_name} Sanic config variable"
                )
            logger.info("[sanic-arq] connecting")

            _redis: ArqRedis = await create_pool(RedisSettings.from_dsn(self._redis_url))
            self.arq_redis = _redis
            logger.info("[sanic-arq] starting worker")
            #await self.arq_redis.enqueue_job('query_user_task')

        @app.listener('after_server_stop')
        async def close_redis(_app, _loop):
            logger.info("[sanic-arq] closing")
            await self.arq_redis.close()


sanic_arq = SanicArq()
