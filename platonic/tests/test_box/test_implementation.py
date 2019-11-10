from platonic import register
from platonic.box import Box, ValueBox


class IntBox(Box[int]):
    pass


@register(IntBox)
class ValueIntBox(ValueBox):
    pass


def test_init():
    assert IntBox(5).value == 5


def test_assign():
    b = IntBox(5)
    b.value = 8
    assert b.value == 8
