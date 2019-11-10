import typing

import pytest

from platonic import Mapping, register, Model


class Marks(Mapping[str, int]):
    pass


@register(Marks)
class DictMarks(dict):
    pass


class Majors(Mapping):
    pass


@register(Majors)
class DictMajors(dict):
    pass


def test_class_getitem():
    subclass = Mapping[str, str]
    assert subclass.__name__ == 'Mapping[str, str]'


def test_overlap():
    assert Majors.__type_args__ is None
    assert Marks.__type_args__ == (str, int)

    marks = Marks()
    assert marks.KeyType is str
    assert marks.ValueType is int

    with pytest.raises(TypeError):
        majors = Majors()

        assert Majors.KeyType is typing.Any
        assert Majors.ValueType is typing.Any
