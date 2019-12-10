import heapq
import itertools
import operator

from typing import Iterable, Optional

from platonic_sorted.base import KeyFunction, T, U
from platonic_sorted.subtract import subtract_sorted_iterators
from platonic_sorted.unique import deduplicate_sorted_iterable


class Sorted(Iterable[T]):
    iterable: Iterable[T]
    key: Optional[KeyFunction] = None
    reverse: bool = False

    def __init__(
            self,
            iterable: Iterable[T],
            key: Optional[KeyFunction] = None,
            reverse=None
    ):
        """
        Declare `iterable` as a container sorted by `key` function.
        """
        self.iterable = iterable

        if key is not None:
            self.key = key

        if reverse is not None:
            self.reverse = reverse

    def __iter__(self):
        return iter(self.iterable)

    def sorting_direction_readable_name(self):
        return 'descending' if self.reverse else 'ascending'

    def __str__(self):
        return (
            f'Sorted({self.iterable}, key={self.key} '
            f'{self.sorting_direction_readable_name()})'
        )

    def unique(self) -> 'Sorted[T]':
        return Sorted(
            deduplicate_sorted_iterable(
                self.iterable,
                key=self.key
            ),
            reverse=self.reverse,
            key=self.key
        )

    def __add__(self, other: 'Sorted[T]') -> 'Sorted[T]':
        return merge(self, other)

    def __sub__(self, other: 'Sorted[U]') -> 'Sorted[T]':
        if self.reverse != other.reverse:
            raise DirectionMismatchError(self, other)

        assert not self.reverse, 'Reversed iterators are not supported yet'

        iterable = subtract_sorted_iterators(
            universe=iter(self.iterable),
            subtracted=iter(other.iterable),

            universe_key=self.key,
            subtracted_key=self.key
        )

        return Sorted(
            iterable,
            key=self.key,
            reverse=self.reverse
        )


def merge(*sorted_iterables: Sorted[T]) -> Sorted[T]:
    """Merge two or more iterators which are known to be sorted."""

    iterables_count = len(sorted_iterables)
    if iterables_count == 0:
        return Sorted([])

    elif iterables_count == 1:
        return sorted_iterables[0]

    first = sorted_iterables[0]
    if not all(i.reverse == first.reverse for i in sorted_iterables):
        raise DirectionMismatchError(*sorted_iterables)

    if not all(i.key == first.key for i in sorted_iterables):
        raise KeyFunctionMismatchError(*sorted_iterables)

    iterable = heapq.merge(
        *sorted_iterables,
        key=first.key,
        reverse=first.reverse
    )

    return Sorted(
        iterable,
        key=first.key,
        reverse=first.reverse
    )


class DirectionMismatchError(Exception):
    def __init__(self, *sorted_iterables: Sorted[T]):
        self.sorted_iterables = sorted_iterables

    def __str__(self):
        count = len(self.sorted_iterables)
        return f'''
Given {count} iterables are incompatible because their sorting directions are
unequal.

  ascending: {', '.join(str(i) for i in self.sorted_iterables if not i.reverse)}
  descending: {', '.join(str(i) for i in self.sorted_iterables if i.reverse)}
'''


class KeyFunctionMismatchError(Exception):
    def __init__(self, *sorted_iterables: Sorted[T]):
        self.sorted_iterables = sorted_iterables

    def __str__(self):
        count = len(self.sorted_iterables)
        items = sorted(
            self.sorted_iterables,
            key=lambda iterable: str(iterable.key)
        )

        grouped_items = itertools.groupby(
            items,
            key=operator.attrgetter('key')
        )

        rows = [
            f'  {key}: {", ".join(map(str, iterables))}\n'
            for key, iterables in grouped_items
        ]

        return f'''\
Given {count} iterables are incompatible because their key functions are
unequal.

{"".join(rows)}
'''
