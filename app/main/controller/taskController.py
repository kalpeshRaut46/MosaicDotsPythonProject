from flask import request
from flask_restful import Resource, Api

# from ..util.dto import UserDto
from injector import inject, Injector

from ..service.taskService import get_all_tasks, RequestHandler
from ..util.db_module import DatabaseModule, configure_for_testing


# api = Api(app)
# _user = UserDto.user


# @api.route('/')
class TaskList(Resource):
    # @api.doc('List of all Tasks')
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all tasks"""
        # return "Hello"
        # return get_all_tasks()
        injector = Injector([configure_for_testing, DatabaseModule()])
        handler = injector.get(RequestHandler)
        return handler.get()
    # @inject
    # def __init__(self, rh: RequestHandler):
    #     self.rh = rh
    #
    # def get(self):
    #     return self.rh.get()


