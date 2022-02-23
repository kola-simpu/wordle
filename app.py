from flask import Flask

from routes import apply_routes
import logging
import os

logging.basicConfig(filename=os.getenv('LOG_FILE', default='wordle.log'), level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
apply_routes(app)

if __name__ == '__main__':
    app.run()
