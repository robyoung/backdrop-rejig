import json
import datetime

import bson
from flask import current_app, request


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        # TODO: this should be added to the chain by the mongodb driver
        if isinstance(obj, bson.ObjectId):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def jsonify(**data):
    """Override Flask's jsonify
    Taken from flask.helpers.jsonify to add JSONEncoder.
    TODO: This can be fixed in a much better way when flask 0.10 is released.
    """
    return current_app.response_class(
        dumps(data, request.is_xhr),
        mimetype='application/json')


def dumps(data, indent=False):
    return json.dumps(data, cls=JsonEncoder, indent=2 if indent else None)