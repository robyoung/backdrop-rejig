import collections

from .errors import BackdropError
from .validation import bucket_name_is_valid


class Bucket(object):
    def __init__(self, db, bucket_name):
        if not bucket_name_is_valid(bucket_name):
            raise InvalidBucketError(
                'Bucket name "{0}" is not valid'.format(bucket_name))

        self._db = db
        self._bucket_name = bucket_name

    def store(self, records):
        if not isinstance(records, collections.Iterable):
            records = [records]

        records = [record.add_updated_at() for record in records]

        self._db.store(self._bucket_name, records)


class InvalidBucketError(BackdropError):
    pass