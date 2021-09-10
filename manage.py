import os
import unittest

from flask_injector import FlaskInjector
from flask_migrate import Migrate
from flask_script import Manager
from injector import inject, Injector
from app.main.util.db_module import Configuration, configure_for_testing, DatabaseModule
from app.main import create_app, db
from app.main.models import task
from app.main.service.taskService import RequestHandler

app = create_app(os.getenv('MOSAICDOTS_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

# injector = Injector([configure_for_testing, DatabaseModule()])
# handler = injector.get(RequestHandler)
# manager.add_command('db', MigrateCommand)
# @inject
# @app.route("/task2")
# def get(rh: RequestHandler):
#     return rh.get()
#
#
# FlaskInjector(app, [Configuration.configure, configuretoRequestHandler])


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
