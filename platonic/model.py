from abc import ABC


PROXY_CLASS_ATTRIBUTE = '__is_proxy_class'


class Model(ABC):
    proxy_class: type = None
    __backend__: type = None
    __type_args__ = None
