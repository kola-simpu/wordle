from flask import Flask

from routes import apply_routes

app = Flask(__name__)
apply_routes(app)

if __name__ == '__main__':
    app.run()
