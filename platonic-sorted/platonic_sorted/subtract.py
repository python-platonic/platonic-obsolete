import logging
from typing import Iterator, Optional

from .base import T, U, KeyFunction

logger = logging.getLogger(__name__)


class Exhausted:
    pass


EXHAUSTED = Exhausted()


def next_or(iterator: Iterator, value: Exhausted = EXHAUSTED):
    try:
        return next(iterator)
    except StopIteration:
        return value


def subtract_sorted_iterators(
        universe: Iterator[T],
        subtracted: Iterator[U],
        universe_key: Optional[KeyFunction] = None,
        subtracted_key: Optional[KeyFunction] = None
) -> Iterator[T]:
    """Return only those items from `universe` which are not present
    in `subtracted`."""

    last_subtracted_element = next_or(subtracted)

    for universe_element in universe:
        if (
            last_subtracted_element == EXHAUSTED
            or universe_element < last_subtracted_element
        ):
            yield universe_element

        else:
            while (
                    last_subtracted_element != EXHAUSTED
                    and universe_element > last_subtracted_element
            ):
                last_subtracted_element = next_or(subtracted)

            if universe_element == last_subtracted_element:
                logger.info('Skipped: %s', universe_element)
                last_subtracted_element = next_or(subtracted)

            else:
                yield universe_element
