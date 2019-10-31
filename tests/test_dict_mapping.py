from abc import ABC

from platonic import register, Mapping
from platonic.mapping import DictMapping


class MyMapping(Mapping):
    pass


@register(MyMapping)
class MyDictMapping(DictMapping):
    pass


def test_dict_mapping():
    m = MyMapping()

    assert isinstance(m, MyDictMapping)

    m['a'] = 'b'

    assert len(m) == 1
    assert m.pop('a') == 'b'
