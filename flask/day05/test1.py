
from flask import Flask


app = Flask(__name__)


# 第一次调用时，才会被执行
@app.before_first_request
def before_first():
    print('before_first')


# 钩子函数
@app.before_request
def before():
    print('before request')


@app.before_request
def before1():
    print('before request1')


@app.route('/index/')
def index():
    return 'index'


# 程序不抛异常/不出错的情况下，才会被调用
@app.after_request
def after(response):
    print('after request')
    return response


@app.after_request
def after(response):
    print('after request1')
    return response


# 无论如何都会执行
@app.teardown_request
def teardown(exception):

    print('teardown request')


if __name__ == '__main__':
    app.run()
