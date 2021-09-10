import sqlalchemy
from injector import Module, provider, Injector, inject, singleton
import sqlite3
from sqlalchemy import create_engine
from app.main import config
from manage import app
import pyodbc


class RequestHandler:
    @inject
    def __init__(self, db: sqlalchemy.engine.Engine):
        self._db = db

    def get(self):
        cursor = self._db.connect()
        print("done")
        data = cursor.execute('SELECT * FROM ProjectTask')
        return data.all()


class Configuration:
    # connection = app.config['SQLALCHEMY_DATABASE_URI']

    def __init__(self, connection):
        self.connection_string = connection


def configure_for_testing(binder):
    configuration = Configuration(app.config['SQLALCHEMY_DATABASE_URI'])
    binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(self, configuration: Configuration) -> sqlalchemy.engine.Engine:
        conn = create_engine(configuration.connection_string)
        # cursor = conn.cursor()
        # cursor.execute('CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)')
        # cursor.execute('INSERT OR REPLACE INTO data VALUES ("hello", "world")')
        return conn


injector = Injector([configure_for_testing, DatabaseModule()])
handler = injector.get(RequestHandler)
data = handler.get()
print(data)
