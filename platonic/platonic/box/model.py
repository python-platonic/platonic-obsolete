from typing import TypeVar

from platonic import Model
from .abstract import AbstractBox


T = TypeVar('T')


class Box(Model, AbstractBox[T]):
    @classmethod
    def __validate_type_args__(cls, args) -> dict:
        value_type, = args
        return {
            'ValueType': value_type
        }
