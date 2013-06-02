from collections import namedtuple
import re
import datetime

from dateutil import parser
import pytz

RESERVED_KEYWORDS = (
    '_timestamp',
    '_id'
)
VALID_BUCKET_RE = re.compile(r'^[a-z][a-z0-9_]+$')
VALID_KEY_RE = re.compile(r'^[a-z_][a-z0-9_]+$')


def bucket_name_is_valid(bucket_name):
    """Test if a bucket name string is valid"""
    return bool(VALID_BUCKET_RE.match(bucket_name.lower()))


def key_is_valid(key):
    key = key.lower()
    if not key:
        return False
    if VALID_KEY_RE.match(key):
        return True
    return False


def key_is_reserved(key):
    return key in RESERVED_KEYWORDS


def key_is_internal(key):
    return key.startswith('_')


def value_is_valid(value):
    return isinstance(value, (int, float, basestring, bool, datetime.datetime))


def value_is_valid_id(value):
    if not isinstance(value, basestring):
        return False
    if re.compile('\s').search(value):
        return False
    return len(value) > 0


# TODO: this is parsing concern not a validation one
def value_is_valid_datetime_string(value):
    return _is_valid_format(value) and _is_real_date(value)


def _is_real_date(value):
    try:
        parser.parse(value).astimezone(pytz.UTC)
        return True
    except ValueError:
        return False


def _is_valid_format(value):
    time_pattern = re.compile(
        "[0-9]{4}-[0-9]{2}-[0-9]{2}"
        "T[0-9]{2}:[0-9]{2}:[0-9]{2}"
        "(?:[+-][0-9]{2}:?[0-9]{2}|Z)"
    )
    return bool(time_pattern.match(value))


## Validation Result

ValidationResult = namedtuple('ValidationResult', 'is_valid message')


def valid():
    return ValidationResult(True, '')


def invalid(message):
    return ValidationResult(False, message)


## Record Validation

def validate_record_data(data):
    for key, value in data.items():
        if not key_is_valid(key):
            return invalid('{0} is not a valid key'.format(key))

        if key_is_internal(key) and not key_is_reserved(key):
            return invalid(
                '{0} is not a recognised internal field'.format(key))

        if not value_is_valid(value):
            return invalid('{0} has an invalid value'.format(key))

        if key == '_timestamp' and not isinstance(value, datetime.datetime):
            return invalid(
                '_timestamp is not a valid datetime object')

        if key == '_id' and not value_is_valid_id(value):
            return invalid('_id is not a valid id')

    return valid()

