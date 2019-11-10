import typing

from platonic import Model


KeyType = typing.TypeVar('KeyType')
ValueType = typing.TypeVar('ValueType')


class MutableMapping(
    Model,
    typing.MutableMapping[KeyType, ValueType]
):
    pass
