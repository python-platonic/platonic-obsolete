import typing

from redis import Redis
from .base import RedisMixin


class RedisMapping(RedisMixin, typing.Mapping):
    name = 'test'

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
