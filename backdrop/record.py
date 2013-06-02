"""Records that can be saved to buckets or partial query stores
"""
from . import timeutils
from .errors import ParseError


def parse_all(data):
    if not isinstance(data, list):
        data = [data]

    return [parse(datum) for datum in data]


def parse(datum):
    """Parse a Record from a python object"""
    if '_timestamp' in datum:
        try:
            datum['_timestamp'] = timeutils._time_string_to_utc_datetime(
                datum['_timestamp'])
        except ValueError:
            raise ParseError(
                '_timestamp is not a valid timestamp, it must be ISO8601')

    return Record(datum)


class Record(object):
    """A record that can be saved to a bucket"""

    def __init__(self, data):
        self.data = data
        self.meta = {}

    def add_updated_at(self):
        self.meta['_updated_at'] = timeutils.now()
        return self

    def to_dict(self):
        return dict(self.data.items() + self.meta.items())


class AggregateRecord(object):
    """An aggregated record that can be saved in a partial query store"""