import os

from flask import Flask

app = Flask(__name__)

app.config.from_object('backdrop.default_settings')
app.config.from_object('backdrop.admin.default_settings')
if os.getenv('FLASK_ENV', 'development') != 'development':
    app.config.from_envvar('BACKDROP_SETTINGS')
    app.config.from_envvar('BACKDROP_ADMIN_SETTINGS')

from . import views