"""
Helpful decorators for Flask views
"""
import functools

from flask import jsonify, request


def json_required(view):
    """Verify a request is JSON and return an error if it is not"""

    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        if request.json is None:
            return jsonify(status='error',
                           message='Expecting JSON payload')
        return view(*args, **kwargs)

    return wrapper

