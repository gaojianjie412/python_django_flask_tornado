
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Student(db.Model):
    # Integer = INTEGER = INT
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), unique=True, nullable=False)
    s_age = db.Column(db.Integer, default=20)
    s_gender = db.Column(db.Boolean, default=1)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def save_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
