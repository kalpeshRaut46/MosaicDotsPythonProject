from injector import Module, provider, Injector, inject, singleton
from app.main import config
from sqlalchemy import create_engine
# from manage import app
from flask import current_app
import sqlalchemy


class Configuration:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def configure_for_testing(binder):
        configuration = Configuration(':memory:')
        binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(self, configuration: Configuration) -> sqlalchemy.engine.Engine:
        engine = create_engine(current_app.config.SQLALCHEMY_DATABASE_URI)
        connection = engine.connect()

        return engine
