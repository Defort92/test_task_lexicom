import aioredis

async def write_data(client: aioredis.Redis, phone: str, address: str):
    await client.set(phone, address)

async def get_address(client: aioredis.Redis, phone: str):
    return await client.get(phone)
