import typing

from redis import Redis


class RedisMapping(typing.MutableMapping):
    url = 'localhost'
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

    def __delitem__(self, key) -> None:
        self.redis.hdel(self.name, key)

    def __setitem__(self, k, v) -> None:
        self.redis.hset(self.name, k, v)
