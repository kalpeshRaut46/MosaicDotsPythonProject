from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import Blueprint, Flask
from flask_injector import FlaskInjector
from injector import Injector

from .controller.taskController import TaskList
from .config import config_by_name
from .util.db_module import Configuration, configure_for_testing, DatabaseModule


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    blueprint = Blueprint('api', __name__)
    app.register_blueprint(blueprint)

    api = Api(app)

    api.add_resource(TaskList, '/tasks')

    # FlaskInjector(app,[Configuration.configure, configuretoRequestHandler])
    return app

