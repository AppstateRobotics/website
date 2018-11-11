#For DBMS expansion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:////tmp/testdb.db'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username