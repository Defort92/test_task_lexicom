from pydantic import BaseSettings

class Settings(BaseSettings):
    redis_hosts: str
    redis_save_interval: str
    redis_appendonly: str
    redis_appendfsync: str

    class Config:
        env_file = ".env"

    def get_redis_startup_nodes(self):
        nodes = []
        hosts = self.redis_hosts.split(',')
        for host in hosts:
            host_info = host.split(':')
            nodes.append(f"redis://{host_info[0]}:{host_info[1]}")
        return nodes


settings = Settings()
