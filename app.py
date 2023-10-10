from flask import Flask
from flask_cors import CORS

# blueprint import
from modules.payments.routes import pay_bp
from modules.users.routes import users_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    
    # # setup all our dependencies
    # database.init_app(app)
    
    # register blueprint
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(pay_bp, url_prefix="/pay")
    
    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0',port=5000,debug=True)