from typing import Mapping
from redis import Redis


class RedisMapping(Mapping):
    url = 'redis://localhost:6379/0'
    name = 'test'

    _connection: Redis = None

    @property
    def redis(self):
        if self._connection is None:
            self._connection = self.create_connection()

        return self._connection

    def create_connection(self):
        return Redis(self.url)

    # Implementing abstract methods

    def __getitem__(self, k):
        value = self.redis.hget(self.name, k)
        if value is None:
            raise KeyError(k)

        else:
            return value

    def __iter__(self):
        return self.redis.hscan_iter(self.name)

    def __len__(self):
        return self.redis.hlen(self.name)
