from flask import Flask
from flask_cors import CORS
from routes.match import match_bp
from routes.history import history_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(match_bp)
    app.register_blueprint(history_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)