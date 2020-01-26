import typing
from abc import ABC

from platonic import Mapping

KeyType = typing.TypeVar('KeyType')
ValueType = typing.TypeVar('ValueType')


# I am not entirely sure how to inherit from a generic type; mypy is very
# unhappy
class MutableMapping(
    Mapping,   # type: ignore
    typing.MutableMapping[KeyType, ValueType],
    ABC
):
    pass
