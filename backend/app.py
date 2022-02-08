from flask import Flask, render_template, jsonify, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
# https://flask-marshmallow.readthedocs.io/en/latest/
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__)
CORS(app)
# load settings from the config.py
app.config.from_object(Config)
# for RESTful api
api = Api(app)
# init for db object
db = SQLAlchemy(app)
# marshmallow converting complex datatypes, such as objects, to and from native Python datatypes
ma = Marshmallow(app)

# Create the database model  https://www.lucidchart.com/pages/database-diagram/database-design#discovery__top
# logical structure of a database and manner data can be stored, organized and manipulated.
class Todo(db.Model):
    # use "Column" to define a column
    id = db.Column('todo_id', db.Integer, primary_key=True)
    content = db.Column(db.String)
    done = db.Column(db.Boolean)
    # def __init__ is optional:
    # sqlalchemy adds an implicit constructor to accept keyword arguments for all its columns and relationships

# integration with Flask-SQLAlchemy and marshmallow-sqlchemy
# ModelSchema that generates fields based the model class meta option
class TodoSchema(ma.SQLAlchemyAutoSchema):
    # class meta options are a way to configure and modify a schemas behavior
    class Meta:
        model = Todo
        load_instance = True

# if the database does not exist, use db.create_all()
def initialize_database():
    try:
        Todo.query.get(1)
    except:
        db.create_all()
        #put some place holder data
        todo1 = Todo(content='buy dildos', done=False)
        todo2 = Todo(content='buy shit', done=False)
        #add then commit changes
        db.session.add(todo1)
        db.session.add(todo2)
        db.session.commit()
        #delete use db.session.delete(me)

def query_database():
    todos = Todo.query.all()
    todos_schema = TodoSchema(many=True)
    #convert the sqlresult into pythonic dict that can be hit with jsonify
    output = todos_schema.dump(todos) #this orginally had .data on the end but was throwing error, should find out why
    return output

def modify_todo( id=-1, content='', done=False, delete=False):
    if id == -1:
        # if the id doesn't match, add new item
        new_todo = Todo(content=content, done=done)
        db.session.add(new_todo)
    else:
        #if the id already exists, modify item
        existing_todo = Todo.query.get(id)
        if delete == True:
            db.session.delete(existing_todo)
        else:
            existing_todo.content = content
            existing_todo.done = done

    # slap them changes boy
    db.session.commit()

class todo_database_access(Resource):
    def get(self):
        # arguments for this function are given by URL
        # curl http://localhost:5000
        output = query_database()
        return jsonify(output)
    def post(self):
        # curl http://localhost:5000/ -d "data=wassup" -X POST -v
        # accept argument by parsing the packages
        # todo_args = parser.parse_args()
        # todo_args = request.get_json()['todo_args']
        todo_args = request.get_json()
        print(todo_args)
        modify_todo(**todo_args)
        return jsonify(status='modify success')

api.add_resource(todo_database_access, '/todo_db')

if __name__ == '__main__':
    initialize_database()
    query_database()
    app.run(debug=True)
