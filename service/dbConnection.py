from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config.dbConfig import DBConfig

db = SQLAlchemy()

def create_flask_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    print(f"Connecting to DB at {app.config['SQLALCHEMY_DATABASE_URI']}")

    db.init_app(app)
    return app