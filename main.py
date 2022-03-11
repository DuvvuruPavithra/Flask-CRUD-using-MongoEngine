from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from models import User

"""
Working with Crud Operations Using Flask and MongoEngine
"""

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'address_book',
    'host': 'localhost',
    'port': 27017
}

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/address_book'
}
db = MongoEngine(app)
db = MongoEngine()
db.init_app(app)


@app.route("/hello/")
def hello():
    return "Hello World! "


@app.route("/add/", methods=['POST'])
def add_user():
    """ Adding The First Contact"""
    details = User(name=request.form["name"], phoneNumber=request.form['phoneNumber'],
                   email=request.form['email'], address=request.form['address'], city=request.form['city'], state=request.form['state'],)
    details.save()
    return jsonify(message="User is added successfully"), 201


@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    body = request.get_json()
    update_contact = User.objects.get(id=id)
    update_contact.update(**body)
    return jsonify(str(update_contact.id)), 200


@app.route('/delete/<id>', methods=["DELETE"])
def delete_user(id):
    """Deleting The Contac t"""
    contact = User.objects.get(id=id)
    contact.delete()
    return jsonify(str(contact.id)), 200


@app.route('/all_users/')
def all_users():
    """Retreiving All contacts"""
    get_contacts = User.objects()
    return jsonify(get_contacts), 200


if __name__ == '__main__':
    app.run(debug=True)
