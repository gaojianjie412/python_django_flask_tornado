
from flask import Flask
from flask_script import Manager

from app.views import blue

app = Flask(__name__)


app = Flask(__name__)
# 第二步：注册蓝图对象
app.register_blueprint(blueprint=blue, url_prefix='/app')

# 管理flask应用对象app
manage = Manager(app)

if __name__ == '__main__':
    # app.run()
    # 启动命令为: python manage.py runserver -h 0.0.0.0 -p 80 -d
    # -h 表示ip地址
    # -p 表示端口
    # -d 表示debug模式
    manage.run()
