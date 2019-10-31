import typing
from abc import ABCMeta, ABC

KeyType = typing.TypeVar('KeyType')
ValueType = typing.TypeVar('ValueType')


class Mapping(typing.Mapping[KeyType, ValueType], ABC):
    pass
