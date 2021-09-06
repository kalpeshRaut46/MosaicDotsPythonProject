from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import Blueprint, Flask

from .controller.taskController import TaskList as task
from .config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    blueprint = Blueprint('api', __name__)

    api = Api(blueprint)

    api.add_resource(task, path='/tasks')
    app.register_blueprint(blueprint)
    return app

