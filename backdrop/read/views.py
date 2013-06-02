from flask import request
from flask_negotiate import produces

from . import app, db
from backdrop.decorators import crossdomain
from ..query import Query
from ..errors import ValidationError, ParseError
from ..jsonutils import jsonify


@app.route('/_status')
def status():
    return "read status"


@app.route('/<bucket_name>')
@produces('application/json')
@crossdomain(origin='*')
@db.load_bucket
def do_query(bucket):
    try:
        result = bucket.query(Query.parse(request.args))

        return jsonify(data=result.data())
    except (ParseError, ValidationError) as e:
        return jsonify(status='error',
                       message=str(e)), 400


@app.route('/<bucket_name>/<partial_name>')
def partial_query(bucket_name, partial_name):
    pass