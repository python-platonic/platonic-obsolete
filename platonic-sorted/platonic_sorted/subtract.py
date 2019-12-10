import itertools
import logging
from collections import namedtuple
from dataclasses import dataclass
from typing import Iterator, Optional, Any

from .base import T, U, KeyFunction

logger = logging.getLogger(__name__)


class Exhausted:
    pass


EXHAUSTED = Exhausted()


@dataclass(frozen=True)
class Caret:
    value: T
    key: Any


def caret(iterator: Iterator[T], key: Optional[KeyFunction]) -> Iterator[Caret]:
    """
    Apply key function to every item in the iterator. After it is complete,
    yield infinite number of EXHAUSTED values.
    """
    if key is None:
        for value in iterator:
            yield Caret(value, value)

    else:
        for value in iterator:
            yield Caret(value, key(value))

    for _ in itertools.count():
        yield EXHAUSTED


def subtract_sorted_iterators(
        universe: Iterator[T],
        subtracted: Iterator[U],
        universe_key: Optional[KeyFunction] = None,
        subtracted_key: Optional[KeyFunction] = None
) -> Iterator[T]:
    """Return only those items from `universe` which are not present
    in `subtracted`."""

    universe_caret = caret(universe, universe_key)
    subtracted_caret = caret(subtracted, subtracted_key)

    second = next(subtracted_caret)

    for first in universe_caret:
        if first == EXHAUSTED:
            return

        # If the second iterator's current value is greater than current first
        # iterator value, we slide along the first iterator.
        if (
            second == EXHAUSTED
            or first.key < second.key
        ):
            yield first.value
            continue

        # If second iterator's current value is greater that that of first
        # iterator, we slide along the second iterator.
        while (
                second != EXHAUSTED
                and first.key > second.key
        ):
            second = next(subtracted_caret)

        # Current values of the two iterators are equal. By definition of
        # subtraction, we do not yield first.value, - we do nothing.
        if (
            second != EXHAUSTED
            and first.key == second.key
        ):
            pass

        else:
            yield first.value
