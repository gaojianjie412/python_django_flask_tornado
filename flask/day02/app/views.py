
from flask import Blueprint, redirect, \
    url_for, abort, render_template, \
    request, make_response, session
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import logout_user, login_required, login_user, login_manager, LoginManager

login_manage = LoginManager()


# 第一步，初始化蓝图对象，并使用对象管理路由
# 初始化蓝图对象，蓝图用于模块化管理路由
from app.models import db, User
from utils.functions import is_login

blue = Blueprint('first', __name__)


# 蓝图对象.route(路由)
@blue.route('/hello/')
def hello():
    return '还有几天放假'

# 路由规则
# <int:id> 表示接收的id值为int类型
# <string:name>表示接收的name参数为string类型，可简写为<name>
# <float:num>
# <uuid:uid>
# <path:path>


@blue.route('/stu/<int:id>')
@is_login
def stu(id):
    return 'hello stu id:%d' % id


@blue.route('/name/<string:name>')
def stu_name(name):
    print(type(name))
    return 'hello stu: %s' % name


@blue.route('/redirect_hello/')
def redirect_hello():
    # 实现重定向
    # 第一种方式
    # return redirect('/app/hello/')
    # 第二种方式：使用url_for的形式进行反向解析
    # url_for ('生成蓝图的第一个参数.重定向的函数名')
    # reverse('namespace:name', kwargs={'id'= id})
    # 无参的跳转
    # return redirect(url_for('first.hello'))
    # 有参的跳转
    return redirect(url_for('first.stu', id=1))


# 抛出错误与处理
@blue.route('/index/')
def index():
    try:
        a = 1
        b = 0
        c = a/b
    except Exception as e:
        abort(500)
    return 'hello'


# 捕获500错误
@blue.errorhandler(500)
def error_500(e):
    return 'exception :%s' % e


@blue.route('/my_index/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@login_required
def my_index():
    if request.method == 'GET':
        # 模版index.html存在于templates文件夹下，
        # 且templates文件夹和manage.py文件同级

        # 接收参数，使用request.args
        # request.args.get(key)或request.args.getlist(key)
        return render_template('index.html')

    if request.method == 'POST':
        # 接收参数
        # 使用request.form取值
        # request.form.get(key)或者request.form.getlist(key)
        pass


@blue.route('/response/', methods=['GET'])
def get_response():
    # 响应字符串
    # res = make_response('<h3>2019毕业</h3>')
    # 响应模版文件
    html = render_template('index.html')
    res = make_response(html, 200)
    # res.set_cookie('token', '1234567890', max_age=10)
    res.delete_cookie('token')
    return res


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 1.获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 2.session的使用
        if username == 'coco' and password == '123456':
            # 模拟登录
            session['user_id'] = 1
            return redirect(url_for('first.stu', id=1))
        return render_template('login.html')


@blue.route('/create_db/')
def create_db():
    # 只能用一次（模型对应的表名不存在于数据库中时，才可使用）
    db.create_all()
    # 删除
    # db.drop_all()
    return '创建表成功'


@blue.route('/my_register/', methods=['GET', 'POST'])
def my_register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        # 获取参数
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        cpwd = request.form.get('cpwd')
        # 验证
        if username and pwd and cpwd:
            # 用户名是否已经注册
            user = User.query.filter(User.name == username).first()
            if user:
                return render_template('register.html',
                                       error_name='用户名已注册')
            if pwd != cpwd:
                return render_template('register.html',
                                       error_pwd='密码和确认密码不一致')
            u = User()
            u.name = username
            u.password = generate_password_hash(pwd)

            db.session.add(u)
            db.session.commit()
            return redirect(url_for('first.my_login'))
        else:
            # 传递的参数有为空的情况
            return render_template('register.html')


@blue.route('/my_login/', methods=['GET', 'POST'])
def my_login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 获取登录的参数
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.name == username).first()
        if user:
            # 校验密码是否一致
            if check_password_hash(user.password, password):
                # 使用flask-login实现登录操作
                # 向session中存键值对，键为user_id,值为id值
                login_user(user)

                return redirect(url_for('first.my_index'))
            else:
                return render_template('login.html',
                                       error_pwd='密码错误')
        else:
            return render_template('login.html',
                                   error_name='用户没有注册，请先注册')


@login_manage.user_loader
def load_user(user_id):
    # 定义被login_manage装饰的回调函数
    # 返回的是当前登录系统的用户对象
    return User.query.filter(User.id == user_id).first()
