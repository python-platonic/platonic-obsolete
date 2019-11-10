from abc import abstractmethod
from typing import TypeVar, Generic, Type, Any

T = TypeVar('T')


class AbstractBox(Generic[T]):
    ValueType: Type[T] = Any

    __marker = object()

    def __init__(self, value: T = __marker):
        if not (value is self.__marker):
            self.value = value

    @property
    @abstractmethod
    def value(self) -> T:
        raise NotImplementedError()

    @value.setter
    @abstractmethod
    def value(self, value: T):
        raise NotImplementedError()
