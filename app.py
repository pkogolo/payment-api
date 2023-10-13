import os

from flask import Flask
from flask_cors import CORS

from config import app_configuration

# blueprint import
from modules.payments.routes import pay_bp
from modules.users.routes import users_bp


def create_app(environment):
    app = Flask(__name__)

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    # setup with the configuration provided
    app.config.from_object(app_configuration[environment])
    # bundle errors at once
    app.config['BUNDLE_ERRORS'] = True

    # landing route
    @app.route('/')
    def index():
        return "Deuce Payment Backend"

    # # setup all our dependencies
    # database.init_app(app)

    # register blueprint
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(pay_bp, url_prefix="/pay")

    return app


# starts the flask application
app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)
