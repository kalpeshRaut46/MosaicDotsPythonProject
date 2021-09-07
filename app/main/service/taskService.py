import uuid
import datetime
import urllib
from flask import current_app
from sqlalchemy import create_engine
from app.main import config
from app.main.util import db_module
from injector import Module, provider, Injector, inject, singleton
# from app.main import db
from app.main.models.task import ProjectTask
# from manage import app
import sqlalchemy


def get_all_tasks():
    # return "Hello"
    tasks = ProjectTask.query.all()
    return tasks


class RequestHandler:

    # def __init__(self, db: sqlalchemy.engine.Engine):
    #     self._db = db

    def get(self):
        # current_app
        engine = create_engine('mssql+pyodbc://dbadmin:4zK#wR*=@mosaicdotsconstructions.database.windows.net/MosaicDotsConstructions?driver=ODBC Driver 17 for SQL Server?Trusted_Connection=yes')
        con = engine.connect()
        # cursor = con.cursor()
        result = engine.execute("SELECT * FROM ProjectTask")
        result.close()
        return result.fetchall()
