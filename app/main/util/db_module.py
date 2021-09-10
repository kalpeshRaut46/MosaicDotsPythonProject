from flask_injector import request
from injector import Module, provider, Injector, inject, singleton
from app.main import config
from sqlalchemy import create_engine
# from manage import app
from flask import current_app
import sqlalchemy
from injector import singleton


class Configuration:
    def __init__(self, connection):
        self.connection_string = connection


def configure_for_testing(binder):
    configuration = Configuration(current_app.config['SQLALCHEMY_DATABASE_URI'])
    binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(self, configuration: Configuration) -> sqlalchemy.engine.Engine:
        conn = create_engine(configuration.connection_string)
        cursor = conn.connect()
        # cursor.execute('CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)')
        # cursor.execute('INSERT OR REPLACE INTO data VALUES ("hello", "world")')
        return conn

# class DatabaseModule():
#     # @singleton
#     # @provider
#     def provide_sqlite_connection(self, configuration: Configuration) -> sqlalchemy.engine.Engine:
#         engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
#         # connection = engine.connect()
#
#         return engine
#
#     def __init__(self):
#         self.engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
#         super.__init__()
