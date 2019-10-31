from typing import Mapping
from redis import Redis


class RedisMapping(Mapping):
    url = 'redis://localhost:6379/0'

    _connection: Redis = None

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.create_connection()

        return self._connection

    def create_connection(self):
        return Redis(self.url)

    def __getitem__(self, k):
        value = self.connection.get(k)
        if value is None:
            raise KeyError(k)

        else:
            return value
