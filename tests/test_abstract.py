from abc import abstractmethod

from platonic import Model, register


class Cat(Model):
    @abstractmethod
    def meow(self):
        raise NotImplementedError()


# noinspection PyMethodMayBeStatic
@register(Cat)
class CatBackend:
    def meow(self):
        return 'meow'


def test_inherit():
    assert Cat().meow() == 'meow'
