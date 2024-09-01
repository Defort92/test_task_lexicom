from rediscluster import RedisCluster
from app.config import settings

def get_redis_client():
    startup_nodes = settings.get_redis_startup_nodes()
    client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    return client
