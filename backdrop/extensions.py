"""Flask extensions"""
import functools

from flask import current_app, jsonify

from . import database
from .bucket import Bucket, InvalidBucketError


class Database(object):
    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if 'backdrop.database' not in app.extensions:
            app.extensions['backdrop.database'] = {}

        app.extensions['backdrop.database'] = database.from_config(app.config)

    @property
    def db(self):
        return current_app.extensions['backdrop.database']

    def raw_queries_allowed(self, bucket_name):
        raw_queries_config = current_app.config.get('RAW_QUERIES_ALLOWED', {})
        return bool(raw_queries_config.get(bucket_name, False))

    def load_bucket(self, view):
        """Resolve a bucket name and provide bucket instance to view"""

        @functools.wraps(view)
        def wrapper(*args, **kwargs):
            try:
                bucket_name = kwargs.pop('bucket_name')
                kwargs['bucket'] = Bucket(
                    self.db,
                    bucket_name,
                    self.raw_queries_allowed(bucket_name))

                return view(*args, **kwargs)
            except InvalidBucketError:
                # TODO: handle html requests as well
                return jsonify(status='error',
                               message='invalid bucket name'), 400

        return wrapper

