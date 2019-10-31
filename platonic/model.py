from abc import ABC


class Model(ABC):
    __backend__: type = None

    def __new__(cls, *args, **kwargs):
        print('__new__')

        concrete_class = cls.__backend__
        abstract_class = cls

        if concrete_class is None:
            raise TypeError(
                f'{abstract_class} does not have a backend defined. Please use '
                f'platonic.register() decorator to assign one.'
            )

        bases = (
            concrete_class,
            abstract_class
        )

        class_name = f'{abstract_class.__name__} via {concrete_class.__name__}'

        # noinspection PyTypeChecker
        proxy_class = type(class_name, bases, {})

        return super(Model, cls).__new__(proxy_class, *args, **kwargs)
