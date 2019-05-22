from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.Integer)

class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users

@app.route('/')
def index():
    return 'Esta es la página principal'

@app.route('/post')
def post():
    new_post = Users(name="Jose Ignacio Huby Ochoa", password=12345)
    db.session.add(new_post)
    db.session.commit()
    return 'Se posteo'

@app.route("/users")
def select_default():
    users = Users.query.all()
    users_schema = UsersSchema(many=True)
    output = users_schema.dump(users).data
    return jsonify({'users' : output})

if __name__ == "__main__":
    db.create_all();
    app.run(port=8000);
