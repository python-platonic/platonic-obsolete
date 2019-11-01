from platonic import MutableMapping, register
from platonic_redis_mapping import RedisMapping


class Cats(MutableMapping):
    pass


@register(Cats)
class RedisCats(RedisMapping):
    pass


def test_init():
    cats = Cats()


def test_assign():
    cats = Cats()

    cats['a'] = 'foo'
    assert cats['a'] == 'foo'


