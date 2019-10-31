import pytest

from platonic import register, Model


class Cat(Model):
    pass


@register(Cat)
class CatBackend:
    pass


class Dog(Model):
    pass


def test_register_twice():
    try:
        @register(Cat)
        class PussyBackend:
            pass

    except ValueError:
        pass

    else:
        assert False, "Exception not raised"


def test_backend():
    assert Cat.__backend__ == CatBackend


def test_isinstance():
    assert isinstance(Cat(), Cat)


def test_no_backend():
    with pytest.raises(TypeError):
        Dog()
