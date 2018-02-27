from flask import Flask
from flask import request
import json

app = Flask(__name__)
UserId= 0
users= []

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    name = request.form["name"]
    global UserId
    UserId = UserId +1;
    NewUser = {'id' : UserId,
                'name' : name
    }
    users.append(NewUser)
    return json.dumps(NewUser),201

@app.route('/users/<id>',methods=['GET'])
def getUser(id):
    for i in range (0,len(users)):
        if int(users[i]['id']) == int(id):
            return json.dumps(users[i]),200
    return 'No User Found with given ID',404

@app.route('/users/<id>',methods=['DELETE'])
def deleteUser(id):
    #print(id)
    for i in range(len(users)):
        if int(users[i]['id']) == int(id):
            users.remove(users[i])
            return '', 204
    return " ", 404