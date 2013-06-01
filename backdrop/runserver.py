from werkzeug.serving import run_simple

from backdrop.all import admin_app, read_app, write_app, application


admin_app.debug = True
read_app.debug = True
write_app.debug = True

run_simple('localhost', 5000, application,
           use_reloader=True,
           use_debugger=True,
           use_evalex=True)
