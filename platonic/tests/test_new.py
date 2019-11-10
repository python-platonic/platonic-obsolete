import typing
import platonic
import dataclasses


@dataclasses.dataclass(frozen=True)
class Cat:
    color: str
    age: int


class Cats(platonic.MutableMapping[str, Cat]):
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
    assert cats.__type_args__ == (str, Cat)

    cats2 = Cats()
    assert cats.__class__ == cats2.__class__
