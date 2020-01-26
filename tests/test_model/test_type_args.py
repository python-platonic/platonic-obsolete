import typing

import pytest

from platonic import Mapping


class Marks(Mapping[str, int], dict):
    pass


def test_none_parameters():
    with pytest.raises(TypeError):
        Mapping[None]


def test_one_parameter():
    with pytest.raises(TypeError):
        Mapping[int]


def test_key_not_type():
    with pytest.raises(ValueError):
        Mapping[5, str]


def test_value_not_type():
    with pytest.raises(ValueError):
        Mapping[int, 5]


def test_name():
    assert Mapping[str, str].__name__ == 'Mapping[str, str]'
