from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


# 生成连接数据库的对象
db = SQLAlchemy()


class User(db.Model, UserMixin):
    # 定义自增的主键id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 定义长度为10的name字段，类型为字符串，唯一且不能为空
    name = db.Column(db.String(10), unique=True, nullable=False)
    # 定义密码password字段
    password = db.Column(db.String(249), nullable=False)

    __tablename__ = 'flask_user'


