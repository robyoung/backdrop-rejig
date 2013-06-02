import argparse

from backdrop.write import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the backdrop write app')
    parser.add_argument('-p', '--port', type=int, default=5003)
    args = parser.parse_args()

    app.run(debug=True)
