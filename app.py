#Import required packages
from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize app
app = Flask(__name__)
#Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///user_details.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 
#Initialize Database
db = SQLAlchemy(app)
#initialize Marshmallow
ma = Marshmallow(app)


#Table
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


#Marshmallow Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password')

# Initialize schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a user
@app.route('/user', methods=['POST'])
def add_user():
    #get data from request
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    #Instantiate new user
    new_user = User(name, email, password)
    #add new user
    db.session.add(new_user)
    #commit the change to reflect in database
    db.session.commit()
    #return the response
    return user_schema.jsonify(new_user)    #or you can use: return jsonify(user_schema.dump(new_user))


#get all users
@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)                  #or you can write single line: jsonify(users_schema.dump(users)) 


#Put and Delete a specific user. 
#(you can do this like you done for post and get request but here i am doing to show you how to handle multiple methods)
@app.route('/user/<int:id>', methods=['PUT', 'DELETE'])
def put_delete(id):
    if request.method == 'PUT':
        user = User.query.get(id)
        user.name = request.json['name']
        user.email = request.json['email']
        user.password = request.json['password']
        db.session.commit()
        return {'message':'data updated'}

    if request.method=='DELETE':
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return {'message':'data deleted successfully'}



# Run Server
if __name__ == '__main__':
    app.run(debug=True)