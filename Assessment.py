from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import flask_bcrypt

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://ajithd2047:<s0IFJDqwrMPGXplR>@cluster0.iv7n12g.mongodb.net/"
app.config['JWT_SECRET_KEY'] = "s0IFJDqwrMPGXplR"
mongo = PyMongo(app)
bcrypt = flask_bcrypt.Bcrypt(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data['Ajith']
    last_name = data['D']
    email = data['ajith.d2007@gmail.com']
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user_data = {
        'Ajith': first_name,
        'D': last_name,
        'ajith.d2007@gmail.com': email,
        'password': password,
    }

    user_id = mongo.db.users.insert(user_data)
    access_token = create_access_token(identity=str(user_id))
    return jsonify(message='User registered successfully', access_token=access_token), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['ajith.d2007@gmail.com']
    password = data['password']

    user = mongo.db.users.find_one({'ajith.d2007@gmail.com': email})

    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify(message='Logged in successfully', access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401

@app.route('/template', methods=['POST'])
@jwt_required
def insert_template():
    data = request.get_json()
    template_name = data['template_name']
    subject = data['subject']
    body = data['body']

    template_data = {
        'template_name': template_name,
        'subject': subject,
        'body': body,
        'user_id': get_jwt_identity(),
    }

    template_id = mongo.db.templates.insert(template_data)
    return jsonify(message='Template added successfully', template_id=str(template_id)), 201

@app.route('/template', methods=['GET'])
@jwt_required
def get_all_templates():
    user_id = get_jwt_identity()
    templates = list(mongo.db.templates.find({'user_id': user_id}, {'user_id': 0}))
    return jsonify(templates), 200

@app.route('/template/<template_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def template(template_id):
    user_id = get_jwt_identity()
    template = mongo.db.templates.find_one({'_id': template_id, 'user_id': user_id}, {'user_id': 0})

    if not template:
        return jsonify(message='Template not found'), 404

    if request.method == 'GET':
        return jsonify(template), 200

    if request.method == 'PUT':
        data = request.get_json()
        mongo.db.templates.update_one({'_id': template_id}, {'$set': data})
        return jsonify(message='Template updated successfully'), 200

    if request.method == 'DELETE':
        mongo.db.templates.delete_one({'_id': template_id})
        return jsonify(message='Template deleted successfully'), 200
