import typing

from .redis_mapping import RedisMapping


class RedisMutableMapping(RedisMapping, typing.MutableMapping):
    def __delitem__(self, key) -> None:
        self.redis.hdel(self.name, key)

    def __setitem__(self, k, v) -> None:
        self.redis.hset(self.name, k, v)
