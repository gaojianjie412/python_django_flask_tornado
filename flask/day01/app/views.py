
from flask import Blueprint, redirect, \
    url_for, abort, render_template, \
    request, make_response


# 第一步，初始化蓝图对象，并使用对象管理路由
# 初始化蓝图对象，蓝图用于模块化管理路由


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




