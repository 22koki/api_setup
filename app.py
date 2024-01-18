from flask import Flask
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



class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            return {"user_id": user_id, "username": "name"}
        else:
            return {"message": "Welcome new user!"}

# Modified route definition to include an optional user_id parameter
api.add_resource(UserResource, '/', '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
