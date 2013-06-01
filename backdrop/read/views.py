from . import app


@app.route('/_status')
def status():
    return "read status"


@app.route('/<bucket_name>')
def query(bucket_name):
    pass


@app.route('/<bucket_name>/<partial_name>')
def partial_query(bucket_name, partial_name):
    pass