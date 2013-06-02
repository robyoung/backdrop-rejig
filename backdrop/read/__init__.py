import os

from flask import Flask

from .. import extensions

app = Flask(__name__)

app.config.from_object('backdrop.default_settings')
app.config.from_object('backdrop.write.default_settings')
if os.getenv('FLASK_ENV', 'development') != 'development':
    app.config.from_envvar('BACKDROP_SETTINGS')
    app.config.from_envvar('BACKDROP_READ_SETTINGS')

db = extensions.Database(app)

from . import views