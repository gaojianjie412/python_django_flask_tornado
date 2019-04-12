
from flask import Flask
from flask_script import Manager
from flask_session import Session
import redis

from app.models import db
from app.views import blue, login_manage

app = Flask(__name__)


app = Flask(__name__)
# 第二步：注册蓝图对象
app.register_blueprint(blueprint=blue, url_prefix='/app')

# 设置加密的复杂程度
app.secret_key = 'fwoe@*!2jo41200sfs23490284**^*^^*#fksef'

# 配置flask-session库，存储数据在redis中
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 初始化配置信息
# 第一种方式
# Session(app)
# 第二种方式
se = Session(app)
se.init_app(app)

# 配置数据库
# mysql+pymysql://root:123456@127.0.0.1:3306/flask8
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库的连接信息
db.init_app(app)

# 初始化登录flask-login
login_manage.init_app(app)


# 管理flask应用对象app
manage = Manager(app)

if __name__ == '__main__':
    # app.run()
    # 启动命令为: python manage.py runserver -h 0.0.0.0 -p 80 -d
    # -h 表示ip地址
    # -p 表示端口
    # -d 表示debug模式
    manage.run()



