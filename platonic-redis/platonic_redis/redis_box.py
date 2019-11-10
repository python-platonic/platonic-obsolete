from typing import TypeVar, Optional

from platonic.box import AbstractBox
from .base import RedisMixin

T = TypeVar('T')


class RedisBox(RedisMixin, AbstractBox[T]):
    name: str
    encoding = 'utf-8'

    def deserialize(self, raw_value: Optional[bytes]) -> T:
        if raw_value is None:
            return self.ValueType()
        else:
            return raw_value.decode(self.encoding)

    def serialize(self, value: T) -> bytes:
        return bytes(value, encoding=self.encoding)

    @property
    def value(self) -> T:
        return self.deserialize(self.redis.get(self.name))

    @value.setter
    def value(self, value: T):
        # FIXME str() is not necessarily the best serialization to hardcode
        self.redis.set(self.name, self.serialize(value))
