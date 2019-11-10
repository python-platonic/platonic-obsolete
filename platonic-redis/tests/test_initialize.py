from platonic import MutableMapping, register
from platonic_redis import RedisMutableMapping
import typing_inspect


class Cats(MutableMapping[str, str]):
    pass


@register(Cats)
class RedisCats(RedisMutableMapping):
    pass


def test_init():
    cats = Cats()


def test_assign():
    cats = Cats()

    raise Exception(Cats.type_args)
