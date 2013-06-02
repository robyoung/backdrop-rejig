import argparse

from werkzeug.serving import run_simple

from backdrop.all import admin_app, read_app, write_app, application


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run all the backdrop apps')
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()

    admin_app.debug = True
    read_app.debug = True
    write_app.debug = True

    run_simple('localhost', args.port, application,
               use_reloader=True,
               use_debugger=True,
               use_evalex=True)
