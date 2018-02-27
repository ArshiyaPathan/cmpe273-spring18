from flask import Flask
from flask import request
import json

app = Flask(__name__)

UserId= 0
Users= []

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
    Users.append(NewUser)
    return json.dumps(NewUser),201

@app.route('/users/<id>',methods=['GET'])
def getUser(id):
     for i in range (len(Users)):
        if Users[i]['id'] == id:
            print(json.dumps(Users[i]))
            return json.dumps(Users[i]),200
        else:
            return 'No User Found with ID', 404

@app.route('/users/<id>',methods=['DELETE'])
def deleteUser(id):
    for i in range(len(Users)):
        if Users[i]['id'] == id:
            Users.remove(Users[i])
            return '', 204
        else:
            return " ", 204