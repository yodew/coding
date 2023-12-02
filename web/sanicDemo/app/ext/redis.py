from sanic_redis import SanicRedis

# redis缓存
redis_cache = SanicRedis()
# redis消息队列
redis_pb = SanicRedis(config_name="REDIS_P_B")
