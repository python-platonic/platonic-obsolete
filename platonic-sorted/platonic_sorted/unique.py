from typing import Iterable, Optional

from .base import KeyFunction, T


class Unknown:
    pass


def deduplicate_sorted_iterable(
        iterable: Iterable[T], key: Optional[KeyFunction] = None
) -> Iterable[T]:
    previous_key_value = Unknown
    for item in iterable:
        key_value = key(item) if key is not None else item

        if key_value == previous_key_value:
            continue

        else:
            previous_key_value = key_value
            yield item
