import argparse

from backdrop.admin import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the backdrop admin app')
    parser.add_argument('-p', '--port', type=int, default=5001)
    args = parser.parse_args()

    app.run(debug=True, port=args.port)
