from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from webapp.config import DATABASE,PASSWORD,USER,HOSTNAME,SECRET_KEY

# db variable initialization
db = SQLAlchemy()

# app initialization
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME,DATABASE)

    Bootstrap(app)
    db.init_app(app)

    from webapp import models
    from webapp.controllers import myapp as myapp

    app.register_blueprint(myapp)

    return app

# Initialization function to create db on a new machine
def create_db():
            import sqlalchemy
            engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
            engine.execute("CREATE DATABASE IF NOT EXISTS %s ;"%(DATABASE))
            engine.execute("USE %s ;" % (DATABASE))
            engine.execute("CREATE TABLE IF NOT EXISTS exchange_rates(from_country VARCHAR(30),to_country VARCHAR(30),date VARCHAR(10),rate DOUBLE(12,4) DEFAULT NULL,PRIMARY KEY (from_country,to_country,date));")

            return engine
