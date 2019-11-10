import typing
from abc import ABC

import platonic


class Cats(platonic.MutableMapping, ABC):
    pass


@platonic.register(Cats)
class CatsBackend(typing.MutableMapping):
    def __delitem__(self, v) -> None:
        pass

    def __getitem__(self, k):
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self):
        pass

    def __setitem__(self, k, v) -> None:
        pass


def test_initialize():
    cats = Cats()
    assert isinstance(cats, Cats)
    assert isinstance(cats, CatsBackend)
    assert cats.__class__.__name__ == 'Cats via CatsBackend'
    assert cats.type_args == ()

    cats2 = Cats()
    assert cats.__class__ == cats2.__class__
