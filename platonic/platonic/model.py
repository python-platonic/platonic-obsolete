from abc import ABC


PROXY_CLASS_ATTRIBUTE = '__is_proxy_class'


def create_proxy_class(cls):
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
    return type(class_name, bases, {
        PROXY_CLASS_ATTRIBUTE: True
    })


class Model(ABC):
    __backend__: type = None
    proxy_class: type = None

    def __new__(cls, *args, **kwargs):
        if getattr(cls, PROXY_CLASS_ATTRIBUTE, False):
            return super().__new__(cls, *args, **kwargs)

        if cls.proxy_class is None:
            cls.proxy_class = create_proxy_class(cls)

        concrete_class = cls.__backend__

        return concrete_class.__new__(cls.proxy_class, *args, **kwargs)
