import json
import uuid
import datetime
import urllib
from flask import current_app, jsonify
from flask_injector import request
from sqlalchemy import create_engine
from app.main import config
from app.main.util import db_module
from injector import Module, provider, Injector, inject, singleton
# from app.main import db
from app.main.models.task import ProjectTask
# from manage import app
import sqlalchemy
import pyodbc

from app.main.util.db_module import DatabaseModule, Configuration


def get_all_tasks():
    # return "Hello"
    tasks = ProjectTask.query.all()
    return tasks


class RequestHandler:
    @inject
    def __init__(self, db: sqlalchemy.engine.Engine):
        self.db = db

    def get(self, json_util=None):
        # current_app
        # engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
        # con = self.engine.connect()
        cursor = self.db.connect()
        result = cursor.execute('SELECT * FROM ProjectTask')
        # for row in result:
        #     print(row)
        # print(result)
        # return json.dumps(result.__class__)
        return jsonify({'result': [dict(row) for row in result]})


# def configuretoRequestHandler(binder):
#     binder.bind(RequestHandler, to=RequestHandler, scope=request)
# injector = Injector([Configuration.configure_for_testing, DatabaseModule()])
# handler = injector.get(RequestHandler)
