from flask import Flask  
from .extensions import db
from .routes import shortener
def create_app(config_file = 'settings.py'):
    app = Flask(__name__) # some tye of skeleton, used to initialize the flask application,
                          # __name__ is a special python variable, 

    app.config.form_pyfile(config_file)  # some standared way of initializing a flask app
    db.init_app(app)

    app.register_blueprint(shortener)

    return app