from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Tasks(Resource):
    tasks = {}
    task_id_counter = 1

    def get(self, task_id=None):
        if task_id:
            task = self.tasks.get(task_id)
            if task:
                return {task_id: task}
            else:
                return {"message": f"Task with ID {task_id} not found"}
        else:
            return {'tasks': self.tasks}

    def post(self):
        task_id = Tasks.task_id_counter
        title = request.json.get('title', '')
        task = {'id': task_id, 'title': title}
        Tasks.tasks[task_id] = task
        Tasks.task_id_counter += 1
        return task

    def put(self, task_id):
        task = Tasks.tasks.get(task_id)
        if not task:
            return {'message': f'Task with ID {task_id} not found'}
        else:
            for key, value in request.json.items():
                task[key] = value
            return task

    def delete(self, task_id):
        if task_id in Tasks.tasks:
            del Tasks.tasks[task_id]
            return {'message': f'Task with ID {task_id} has been deleted'}
        else:
            return {'message': f'Task with ID {task_id} not found'}

class Welcome(Resource):
    def get(self):
        return {"message": "Welcome to the task application!"}

class About(Resource):
    def get(self):
        return {"message": "This is a simple task management API."}

class TaskList(Resource):
    def get(self):
        return {"tasks": list(Tasks.tasks.values())}

class TaskComplete(Resource):
    def get(self, task_id):
        task = Tasks.tasks.get(task_id)
        if task:
            return {"message": f'Task with ID {task_id} is marked as {"completed" if task.get("completed") else "incomplete"}'}
        else:
            return {"message": f'Task with ID {task_id} not found'}

    def put(self, task_id):
        task = Tasks.tasks.get(task_id)
        if task:
            task['completed'] = True
            return {"message": f'Task with ID {task_id} marked as completed'}
        else:
            return {"message": f'Task with ID {task_id} not found'}

class TaskDueDate(Resource):
    def get(self, task_id=None):
        if task_id is not None:
            task = Tasks.tasks.get(task_id)
            if task:
                due_date = task.get('due_date', '')
                return {"message": f'Due date for task with ID {task_id}: {due_date}'}
            else:
                return {"message": f'Task with ID {task_id} not found'}
        else:
            all_due_dates = {task_id: task.get('due_date', '') for task_id, task in Tasks.tasks.items()}
            return {"due_dates": all_due_dates}

    def put(self, task_id):
        task = Tasks.tasks.get(task_id)
        if task:
            due_date = request.json.get('due_date', '')
            task['due_date'] = due_date
            return {"message": f'Due date updated for task with ID {task_id}'}
        else:
            return {"message": f'Task with ID {task_id} not found'}


api.add_resource(TaskDueDate, '/due-date', '/due-date/<int:task_id>')

class CompleteLastTask(Resource):
    def get(self):
        tasks = Tasks.tasks
        if tasks:
            last_task_id = max(tasks.keys())
            task = tasks[last_task_id]
            return task
        else:
            return {"message": "No tasks found"}

api.add_resource(CompleteLastTask, '/complete')     
api.add_resource(Welcome, '/')
api.add_resource(About, '/about')
api.add_resource(Tasks, '/tasks', '/tasks/<int:task_id>')
api.add_resource(TaskList, '/tasks/list')
api.add_resource(TaskComplete, '/complete/<int:task_id>/')


if __name__ == '__main__':
    app.run(debug=True)
