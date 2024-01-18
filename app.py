from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Creating a resource class that inherits from Resource
class GoodMorning(Resource):
    def get(self):
        return {"message": "Good morning! How are you today?"}

# Adding the URL route and the method to be called when this route is accessed
api.add_resource(GoodMorning, '/')


if __name__ == '__main__':
    app.run(debug=True)
