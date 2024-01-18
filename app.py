from flask import Flask, request
from flask_restful import Api, Resource
import os
from flask import Flask, jsonify

app = Flask(__name__)
api = Api(app)

# Creating a resource class that inherits from Resource
#class GoodMorning(Resource):
    #def get(self):
       # return {"message": "Good morning! How are you today?"}
#handling post request
    #def post(self):
       # return {"message":f"Good Morning !  Data recieved:"}
#handling patch request
   # def patch(self,name=""):
       # return {"message": f"Hello {name}, how are you doing? Patch Request!"}
#handling a put request
   # def put(self):
        #return {"message":"I am putting data"}
       
# Adding the URL route and the method to be called when this route is accessed
#api.add_resource(GoodMorning, '/')




#class UserResource(Resource):
 #   def get(self, user_id=None):
  #      if user_id:
   #         return {"user_id": user_id, "username": "name"}
    #    else:
     #       return {"message": "Welcome to the root URL!"}
#
## Modified route definition to include an optional user_id parameter
#api.add_resource(UserResource, '/', '/user/<int:user_id>')


#FLASKRESTFUL FOR HANDLING TASK OPERATIONS LIKE CREATING UPDATING AND MARKING TASKS AS COMPLETED
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


api.add_resource(Tasks, '/', '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)

       
