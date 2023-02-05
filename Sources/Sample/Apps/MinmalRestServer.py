from flask import Flask

from flask_restful import Resource, Api

from Sample.RestResources.HelloWorld import HelloWorld

app = Flask(__name__)

api = Api(app)


api.add_resource(HelloWorld, "/hello")

if __name__ == "__main__":
    app.run(port=5001)