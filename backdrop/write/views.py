from flask import request, jsonify
from flask_negotiate import consumes

from . import app, db
from .. import record, csvutils
from ..errors import ParseError, ValidationError


@app.route('/_status')
def status():
    return "write status"


@app.route('/<bucket_name>', methods=['POST'])
@consumes('application/json', 'text/csv')
@db.load_bucket
def store(bucket):
    try:
        if request.mimetype == 'text/csv':
            data = csvutils.parse(request.data)
        else:
            data = request.json

        bucket.store(record.parse_all(data))
        return jsonify(status='ok')
    except (ParseError, ValidationError) as e:
        return jsonify(status='error',
                       message=str(e)), 400


@app.route('/<bucket_name>/<partial_name>', methods=['POST', 'PUT', 'DELETE'])
def create_partial(bucket_name, partial_name):
    pass
