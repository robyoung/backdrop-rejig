import re

VALID_BUCKET_RE = re.compile(r'^[a-z][a-z0-9_]+$')


def bucket_name_is_valid(bucket_name):
    """Test if a bucket name string is valid"""
    return bool(VALID_BUCKET_RE.match(bucket_name.lower()))