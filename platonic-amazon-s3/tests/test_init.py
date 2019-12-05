import itertools

import pytest

from platonic_amazon_s3 import S3RecursiveKeyStream


class TestKeyStream(S3RecursiveKeyStream):
    url = 's3://homo-yetiensis'


@pytest.mark.skip('Integration test')
def test_initialize():
    piece = itertools.islice(
        TestKeyStream(),
        10
    )

    for item in piece:
        print(item)
