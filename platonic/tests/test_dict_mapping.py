from abc import ABC

from platonic import register, MutableMapping
from platonic.mapping import DictMapping


class MyMapping(MutableMapping):
    pass


@register(MyMapping)
class MyDictMapping(DictMapping):
    pass


def test_dict_mapping():
    m = MyMapping()

    assert isinstance(m, MyDictMapping)
    assert m.__class__.__name__ == 'MyMapping via MyDictMapping'

    m['a'] = 'b'

    assert len(m) == 1
    assert m.pop('a') == 'b'
