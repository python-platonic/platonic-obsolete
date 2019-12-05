from urllib.parse import urlparse

import boto3
from boto3_type_annotations import s3
from botocore.paginate import PageIterator
from typing import Iterator, TypeVar

from platonic_sorted.sorted import Sorted

T = TypeVar('T')


def identity(value: T) -> T:
    return value


def always(value: T) -> bool:
    return True


class S3SortedKeysIterator(Sorted, Iterator[str]):
    url: str

    def recurse(self) -> Iterator[str]:
        """Stream of all file URLs on Data Lake S3 bucket."""

        client: s3.Client = boto3.client('s3')

        decoded_url = urlparse(self.url)
        bucket_name = decoded_url.netloc

        paginator = client.get_paginator('list_objects_v2')

        page_iterator: PageIterator = paginator.paginate(
            Bucket=bucket_name,
            Prefix=decoded_url.path.lstrip('/'),
        )

        for page in page_iterator:
            records = page.get('Contents', [])

            for record in records:
                key = record['Key']
                yield f's3://{bucket_name}/{key}'

    def __iter__(self):
        return self.recurse()
