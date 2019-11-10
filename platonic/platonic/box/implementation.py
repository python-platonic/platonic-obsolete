from typing import TypeVar

from .abstract import AbstractBox

T = TypeVar('T')


class ValueBox(AbstractBox[T]):
    _value: T

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value
