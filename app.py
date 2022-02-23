from flask import Flask

from routes import apply_routes
import logging
from decouple import config as env

logging.basicConfig(filename=env('LOG_FILE', default='wordle.log'), level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
apply_routes(app)

if __name__ == '__main__':
    app.run()
