from platonic import Mapping, register
from platonic_redis_mapping import RedisMapping


class Cats(Mapping):
    pass


@register(Cats)
class RedisCats(RedisMapping):
    pass


def test_init():
    cats = Cats()
