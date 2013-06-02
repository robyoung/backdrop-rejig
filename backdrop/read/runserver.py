import argparse

from backdrop.read import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the backdrop read app')
    parser.add_argument('-p', '--port', type=int, default=5002)
    args = parser.parse_args()

    app.run(debug=True)