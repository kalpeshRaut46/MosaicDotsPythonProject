from flask import request
from flask_restful import Resource, Api

# from ..util.dto import UserDto
from ..service.taskService import get_all_tasks, RequestHandler


# api = Api(app)
# _user = UserDto.user


# @api.route('/')
class TaskList(Resource):
    # @api.doc('List of all Tasks')
    # @api.marshal_list_with(_user, envelope='data')
    # def get(self):
    #     """List all tasks"""
    #     # return "Hello"
    #     return get_all_tasks()

    def get(self):

        task = RequestHandler()
        return task.get()


