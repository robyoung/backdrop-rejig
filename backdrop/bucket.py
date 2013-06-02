import collections

from . import response
from .errors import BackdropError, ValidationError
from .validation import bucket_name_is_valid


class Bucket(object):
    def __init__(self, db, bucket_name, allow_raw_queries):
        if not bucket_name_is_valid(bucket_name):
            raise InvalidBucketError(
                'Bucket name "{0}" is not valid'.format(bucket_name))

        self._db = db
        self._bucket_name = bucket_name
        self._allow_raw_queries = allow_raw_queries

    def store(self, records):
        if not isinstance(records, collections.Iterable):
            records = [records]

        records = [record.add_updated_at() for record in records]

        self._db.store(self._bucket_name, records)

    def query(self, query):
        if query.is_raw_query and not self.allow_raw_queries:
            raise ValidationError("querying for raw data is not allowed")

        result = self._db.query(self._bucket_name, query)

        if query.is_period_grouped_query:
            result = response.build_period_group_response(query, result)
        elif query.is_grouped_query:
            result = response.build_grouped_response(result)
        elif query.is_period_query:
            result = response.build_period_response(query, result)
        else:
            result = response.build_simple_response(result)
        return result

    @property
    def allow_raw_queries(self):
        return self._allow_raw_queries


class InvalidBucketError(BackdropError):
    pass