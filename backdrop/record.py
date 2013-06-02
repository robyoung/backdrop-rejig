"""Records that can be saved to buckets or partial query stores
"""
from . import timeutils
from .timeseries import WEEK, MONTH
from .validation import validate_record_data
from .errors import ParseError, ValidationError


def parse_all(data):
    if not isinstance(data, list):
        data = [data]

    return [parse(datum) for datum in data]


def parse(datum):
    """Parse a Record from a python object"""
    if '_timestamp' in datum:
        try:
            datum['_timestamp'] = timeutils.parse_time_string(
                datum['_timestamp'])
        except ValueError:
            raise ParseError(
                '_timestamp is not a valid timestamp, it must be ISO8601')

    return Record(datum)


class Record(object):
    """A record that can be saved to a bucket"""

    def __init__(self, data):
        result = validate_record_data(data)
        if not result.is_valid:
            raise ValidationError(result.message)

        self.data = data
        self.meta = {}

        if "_timestamp" in self.data:
            self.meta['_week_start_at'] = WEEK.start(self.data['_timestamp'])
            self.meta['_month_start_at'] = MONTH.start(self.data['_timestamp'])

    def add_updated_at(self):
        self.meta['_updated_at'] = timeutils.now()
        return self

    def to_dict(self):
        return dict(self.data.items() + self.meta.items())


class AggregateRecord(object):
    """An aggregated record that can be saved in a partial query store"""