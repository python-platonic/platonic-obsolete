import typing

from platonic import Model

ValueType = typing.TypeVar('ValueType')


class Iterable(typing.Iterable[ValueType], Model):
    pass
