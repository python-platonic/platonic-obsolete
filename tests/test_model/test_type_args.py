import typing

import pytest

from platonic import Mapping


class Marks(Mapping[str, int], typing.Dict[str, int]):
    pass


def test_none_parameters():
    with pytest.raises(TypeError):
        Mapping[None]   # type: ignore


def test_one_parameter():
    with pytest.raises(TypeError):
        Mapping[int]   # type: ignore


def test_key_not_type():
    with pytest.raises(ValueError):
        Mapping[5, str]   # type: ignore


def test_value_not_type():
    with pytest.raises(ValueError):
        Mapping[int, 5]   # type: ignore


def test_name():
    assert Mapping[str, str].__name__ == 'Mapping[str, str]'
