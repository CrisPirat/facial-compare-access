import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

db = SQLAlchemy()

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    for module_name in ('faceapi',):
        try:
            app.logger.info('registering {}'.format(module_name))
            module = import_module('apps.{}.routes'.format(module_name))
            app.register_blueprint(module.blueprint)
        except Exception as e:
            app.logger.error("Error {}".format(str(e)))

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        try:
            app.logger.info('initialize_database db')
            db.create_all()
        except Exception as e:

            app.logger.error('> Error: DBMS Exception: ' + str(e) )

            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

            app.logger.error('> Fallback to SQLite ')
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def register_handle_errors(app):
    @app.errorhandler(401)
    def unauthorized(e):  
        return "401."
    @app.errorhandler(403)
    def forbidden(e):  
        return "403."
    @app.errorhandler(404)
    def not_found(e):  
        return "404."
    @app.errorhandler(405)
    def method_not_allowed (e):  
        return "405."
    @app.errorhandler(406)
    def not_acceptable(e):  
        return "406."
    @app.errorhandler(412)
    def precondition_failed(e):  
        return "412."   

def create_app(config):
    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    register_handle_errors(app)
    return app

