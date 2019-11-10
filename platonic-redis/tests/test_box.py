from platonic import Box, register
from platonic_redis import RedisBox


class SiteNameBox(Box[str]):
    """Storing our site name"""


@register(SiteNameBox)
class RedisSiteNameBox(RedisBox):
    name = 'site-name'


def test_empty():
    assert SiteNameBox().value is ''


def test_set():
    box = SiteNameBox()
    box.value = 'John Connor'

    assert box.value == 'John Connor'
