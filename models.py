import mongoengine as db

class User(db.Document):
    name = db.StringField(max_length=50, required=True)
    phoneNumber = db.IntField(max_value=99999999, required=True)
    email = db.StringField(max_length=50, required=True)
    address = db.StringField(max_length=10, required=True)
    city = db.StringField(max_length=10, required=True)
    state = db.StringField(max_length=10, required=True)
