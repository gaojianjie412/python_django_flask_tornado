
import pymysql
from flask import Flask, request, g

app = Flask(__name__)


@app.before_request
def before():
    # 链接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           password='123456', user='root',
                           database='flask8')
    # 获取游标
    cursor = conn.cursor()
    # g对象在当前的请求流程当中，相当于全局变量
    g.conn = conn
    g.cursor = cursor


@app.route('/sel_stu/', methods=['GET'])
def sel():
    if request.method == 'GET':

        # 查询所有学生的信息
        sql = 'select * from student'
        g.cursor.execute(sql)
        data = g.cursor.fetchall()
        print(data)

        return '查询成功'


@app.teardown_request
def teardown(exception):
    # 关闭游标
    g.conn.close()


if __name__ == '__main__':
    app.run(debug=True)
