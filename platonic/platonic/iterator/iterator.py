import typing

from platonic import Model


ValueType = typing.TypeVar('ValueType')


class Iterator(typing.Iterator[ValueType], Model):
    pass
