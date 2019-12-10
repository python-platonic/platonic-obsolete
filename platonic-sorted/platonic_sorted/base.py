from typing import Callable, Any, TypeVar

T = TypeVar('T')
U = TypeVar('U')

KeyFunction = Callable[[T], Any]
