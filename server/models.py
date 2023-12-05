from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.String, primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(255), unique=True)
    password= db.Column(db.String)