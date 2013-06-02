import datetime
from dateutil import parser
import pytz


def now():
    return datetime.datetime.now(pytz.UTC)


def _time_string_to_utc_datetime(time_string):
    time = parser.parse(time_string)
    return time.astimezone(pytz.utc)
