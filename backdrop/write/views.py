from flask import request, jsonify

from . import app, db
from .. import record
from ..errors import ParseError, ValidationError
from ..decorators import json_required


@app.route('/_status')
def status():
    return "write status"


@app.route('/<bucket_name>', methods=['POST'])
@json_required
@db.load_bucket
def store(bucket):
    try:
        bucket.store(record.parse_all(request.json))
        return jsonify(status='ok')
    except (ParseError, ValidationError) as e:
        return jsonify(status='error',
                       message=str(e)), 400


@app.route('/<bucket_name>/<partial_name>', methods=['POST', 'PUT', 'DELETE'])
def create_partial(bucket_name, partial_name):
    pass
