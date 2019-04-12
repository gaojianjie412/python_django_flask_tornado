
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
    g_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)
    icon = db.Column(db.String(100), nullable=True)

    def save_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), nullable=False, unique=True)
    # 定义了一个关联关系字段，和反向引用backref参数
    s_g = db.relationship('Student', backref='g')


# 中间表
s_c = db.Table('s_c',
               db.Column('s_id', db.Integer, db.ForeignKey('student.id')),
               db.Column('c_id', db.Integer, db.ForeignKey('course.id'))
               )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(10), unique=True, nullable=False)
    stu = db.relationship('Student', secondary=s_c, backref='cou')
