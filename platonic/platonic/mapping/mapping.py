import typing
from abc import ABC

from platonic import Model


KeyType = typing.TypeVar('KeyType')
ValueType = typing.TypeVar('ValueType')


class Mapping(Model, typing.Mapping[KeyType, ValueType], ABC):
    KeyType: typing.Type = None
    ValueType: typing.Type = None

    @classmethod
    def __validate_type_args__(cls, args):
        if args is None:
            raise TypeError(f'Type args missing for {cls}.')

        elif not isinstance(args, tuple):
            raise ValueError(
                f'Type args for {cls} should be a tuple, {args} found instead.'
            )

        elif len(args) != 2:
            raise ValueError(
                f'Exactly 2 type args expected for {cls}, {args} found instead.'
            )

        cls.KeyType, cls.ValueType = args

        return args
