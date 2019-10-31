from platonic import register, Model


class Cat(Model):
    pass


@register(Cat)
class CatBackend:
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
