from platonic import register, Mapping
from platonic.mapping import DictMapping


@register(Mapping)
class MyDictMapping(DictMapping):
    pass


def test_dict_mapping():
    m = MyDictMapping()

    m['a'] = 'b'

    assert len(m) == 1
    assert m.pop('a') == 'b'
