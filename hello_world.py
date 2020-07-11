#Import required packages
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize app
app = Flask(__name__)

#Create a Hello-World route
@app.route('/hello-world', methods=['GET'])
def get_hello_world():
    return jsonify({'message': 'Hello World'})

# Run Server
if __name__ == '__main__':
    app.run(debug=True)