import aioredis
from app.config import settings


async def get_redis_client():
    startup_nodes = settings.get_redis_startup_nodes()
    client = await aioredis.create_redis_pool(
        startup_nodes,
        decode_responses=True
    )
    return client
