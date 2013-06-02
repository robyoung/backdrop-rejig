from collections import namedtuple
from backdrop.errors import ValidationError
from backdrop.validation import validate_query_args

from .timeutils import parse_time_string


def if_present(func, value):
    if value is not None:
        return func(value)


def parse_request_args(request_args):
    args = dict()

    args['start_at'] = if_present(parse_time_string,
                                  request_args.get('start_at'))

    args['end_at'] = if_present(parse_time_string,
                                request_args.get('end_at'))

    args['filter_by'] = [
        f.split(':', 1) for f in request_args.getlist('filter_by')
    ]

    args['period'] = request_args.get('period')

    args['group_by'] = request_args.get('group_by')

    args['sort_by'] = if_present(lambda sort_by: sort_by.split(':', 1),
                                 request_args.get('sort_by'))

    args['limit'] = if_present(int, request_args.get('limit'))

    args['collect'] = request_args.getlist('collect')

    return args


_Query = namedtuple(
    '_Query',
    'start_at end_at filter_by period group_by sort_by limit collect'
)


class Query(_Query):
    @classmethod
    def create(cls,
               start_at=None, end_at=None, filter_by=None, period=None,
               group_by=None, sort_by=None, limit=None, collect=None):
        return Query(start_at, end_at, filter_by or [], period,
                     group_by, sort_by, limit, collect or [])

    @classmethod
    def parse(cls, request_args):
        result = validate_query_args(request_args)
        if not result.is_valid:
            raise ValidationError(result.message)
        args = parse_request_args(request_args)
        return Query(**args)

    @property
    def is_raw_query(self):
        return not(self.group_by or self.period)

    @property
    def is_period_grouped_query(self):
        return self.group_by and self.period

    @property
    def is_grouped_query(self):
        return self.group_by

    @property
    def is_period_query(self):
        return self.period
