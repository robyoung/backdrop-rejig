from werkzeug.wsgi import DispatcherMiddleware

from .admin import app as admin_app
from .read import app as read_app
from .write import app as write_app

application = DispatcherMiddleware(admin_app, {
    '/read': read_app,
    '/write': write_app,
})
