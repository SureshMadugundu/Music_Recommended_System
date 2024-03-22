from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class StudentModel(db.Model):
    __tablename__="users"

    userid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String())
    password=db.Column(db.String())

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def __repr__(self):

            return f"{self.username}:{self.password}"
