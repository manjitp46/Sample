from flask_restful import Resource, reqparse
from flask import jsonify
from Sample.DataStore.MongoDataStore import MongoDataStore
from Sample.Utils.BaseObject import BaseObject
import logging
logging.basicConfig(level = logging.DEBUG,format = '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')
class StudentRestResource(Resource, BaseObject):

    def __init__(self) -> None:
        Resource().__init__()
        BaseObject().__init__()
        
        self._dataStore = MongoDataStore()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help="Name of the student is required")
        self.parser.add_argument('age', type=int, required=True, help="Age of the student is required")
        self.parser.add_argument('student_id', type=str, required=True, help="ID of the student is required")
        self.parser.add_argument('major', type=str, required=True, help="Major of the student is required")

    def post(self):
        """
        Saves an student recored to database
        # It works also with swag_from, schemas and spec_dict
        ---
        parameters:
          - in: body
            name: student
            description: Student data
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                age:
                  type: integer
                student_id:
                  type: string
                major:
                  type: string
            example:
              name: John Doe
              age: 25
              student_id: "123456"
              major: Computer Science


        responses:
          200:
            description: All Student Data
            # schema:
            #   id: User
            #   properties:
            #     username:
            #       type: string
            #       description: The name of the user
            #       default: Steven Wilson
        """
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
        """
        This end points brings list of students present in database
        # It works also with swag_from, schemas and spec_dict
        ---
        # parameters:
        #   - in: path
        #     name: username
        #     type: string
        #     required: true
        responses:
          200:
            description: All Student Data
            # schema:
            #   id: User
            #   properties:
            #     username:
            #       type: string
            #       description: The name of the user
            #       default: Steven Wilson
        """

        students = self._dataStore.GetAllStudents()
        logging.info("Printed Logging Message")
        # self.Logger.info("Getting All Studensts Records")
        return students, 200
