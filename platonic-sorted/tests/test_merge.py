import pytest
from platonic_sorted import (
    merge, Sorted, DirectionMismatchError, KeyFunctionMismatchError
)


def test_no_arguments():
    assert list(merge()) == []


def test_one_argument():
    s = Sorted([1, 2, 3])
    assert merge(s) == s


def test_two_arguments():
    even = Sorted([0, 2, 4])
    odd = Sorted([1, 3, 5])
    merged = merge(even, odd)
    assert list(merged) == [0, 1, 2, 3, 4, 5]


def test_direction_mismatch():
    with pytest.raises(DirectionMismatchError):
        merge(
            Sorted([1, 2, 3]),
            Sorted([5, 4, 3], reverse=True)
        )


def test_key_function_mismatch():
    with pytest.raises(KeyFunctionMismatchError):
        # noinspection PyTypeChecker
        merge(
            Sorted([1, 2, 3]),
            Sorted(['c', 'bb', 'aaa'], key=len)
        )
