import datetime
from dateutil import parser
import pytz


def now():
    return datetime.datetime.now(pytz.UTC)


def parse_time_string(time_string, default=None):
    if time_string is None:
        return default
    time = parser.parse(time_string)
    return time.astimezone(pytz.utc)


def utc(dt):
    return dt.replace(tzinfo=pytz.UTC)
