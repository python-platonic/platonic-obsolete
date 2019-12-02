from platonic_amazon_s3 import S3SortedKeysIterator


class TestKeyStream(S3SortedKeysIterator):
    pass


def test_initialize():
    stream = TestKeyStream()

    for item in stream:
        print(item)
