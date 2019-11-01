import typing

from platonic import Model


KeyType = typing.TypeVar('KeyType')
ValueType = typing.TypeVar('ValueType')


class MutableMapping(
    typing.MutableMapping[KeyType, ValueType],
    Model
):
    pass
