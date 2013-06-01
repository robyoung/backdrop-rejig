from . import app


@app.route('/_status')
def status():
    return "write status"


@app.route('/<bucket_name>')
def post(bucket_name):
    pass


@app.route('/<bucket_name>/<partial_name>')
def create_partial(bucket_name, partial_name):
    pass
