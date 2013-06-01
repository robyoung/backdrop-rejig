from . import app


@app.route('/')
def index():
    return "Index"


@app.route('/sign-in')
def sign_in():
    pass


@app.route('/sign-out')
def sign_out():
    pass


@app.route('/authorized')
def authorized():
    pass


@app.route('/bucket')
def buckets():
    pass


@app.route('/users')
def users():
    pass


@app.route('/bucket/<bucket_name>')
def bucket(bucket_name):
    pass


@app.route('/bucket/<bucket_name>/upload')
def upload(bucket_name):
    pass
