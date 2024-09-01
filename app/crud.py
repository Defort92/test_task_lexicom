from redis import Redis


def write_data(client: Redis, phone: str, address: str):
    client.set(phone, address)

def get_address(client: Redis, phone: str):
    return client.get(phone)
