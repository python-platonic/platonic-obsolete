import typing
from abc import ABC

from platonic.mapping import Mapping

KeyType = typing.TypeVar('KeyType')
ValueType = typing.TypeVar('ValueType')


class MutableMapping(
    Mapping,
    typing.MutableMapping[KeyType, ValueType],
    ABC
):
    pass
