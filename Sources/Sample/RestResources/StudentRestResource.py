from flask_restful import Resource, reqparse
from flask import jsonify
from Sample.DataStore.MongoDataStore import MongoDataStore
class StudentRestResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self._dataStore = MongoDataStore()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help="Name of the student is required")
        self.parser.add_argument('age', type=int, required=True, help="Age of the student is required")
        self.parser.add_argument('student_id', type=str, required=True, help="ID of the student is required")
        self.parser.add_argument('major', type=str, required=True, help="Major of the student is required")

    def post(self):
        # Parse the arguments from the request
        args = self.parser.parse_args()

        # Get the student data from the request
        name = args['name']
        age = args['age']
        student_id = args['student_id']
        major = args['major']

        # Add the student data to your data store
        # ...
        print(args)
        self._dataStore.AddStudent(args)
        # Return a success message indicating that the student data was posted successfully
        return {'message': 'Student data was posted successfully'}, 201

    def get(self):

        students = self._dataStore.GetAllStudents()

        return students, 200
