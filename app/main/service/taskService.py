import uuid
import datetime
from app.main.util import db_module
from injector import Module, provider, Injector, inject, singleton
# from app.main import db
from app.main.models.task import ProjectTask

import sqlalchemy


def get_all_tasks():
    return ProjectTask.query.all()


class RequestHandler:
    @inject
    def __init__(self, db: sqlalchemy.engine.Engine):
        self._db = db

    def get(self):
        cursor = self._db.cursor()
        cursor.execute('SELECT key, value FROM data ORDER by key')
        return cursor.fetchall()
