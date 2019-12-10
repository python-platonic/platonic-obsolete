from platonic_sorted import KeyFunctionMismatchError, Sorted


def test_print_error():
    err = KeyFunctionMismatchError(
        Sorted([1, 2, 3]),
        Sorted(['a', 'b', 'c'], key=len)
    )

    assert str(err).startswith('Given 2 iterables are incompatible')
