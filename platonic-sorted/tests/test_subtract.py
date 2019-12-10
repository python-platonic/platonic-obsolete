from platonic_sorted import subtract_sorted_iterators


def test_no_key():
    s1 = range(11)
    s2 = iter([5, 10])

    r = subtract_sorted_iterators(s1, s2)

    assert list(r) == [
        0, 1, 2, 3, 4,
        6, 7, 8, 9
    ]


def test_with_keys():
    s1 = range(11)
    s2 = iter([-5, -10])

    r = subtract_sorted_iterators(s1, s2, subtracted_key=abs)

    assert list(r) == [
        0, 1, 2, 3, 4,
        6, 7, 8, 9
    ]


def test_with_repeats():
    s1 = iter([1, 2, 2, 3])
    s2 = iter([2])

    r = subtract_sorted_iterators(s1, s2)

    assert list(r) == [1, 3]
