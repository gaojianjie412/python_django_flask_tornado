
from flask import Blueprint, render_template, request
# from flask_mail import Message

from app.models import Student, db
# from manage import mail

blue = Blueprint('app', __name__)


@blue.route('/')
def hello():
    return 'hello world'


@blue.route('/index/')
def index():
    content_h2 = '<h2>随便写点内容</h2>'
    socres = [34, 404, 90, 89]
    return render_template('index.html', a=content_h2, b=socres)


@blue.route('/add_stu/', methods=['GET'])
def add_stu():
    if request.method == 'GET':
        # 插入数据
        stu = Student()
        stu.s_name = '莉哥'
        stu.s_gender = 0
        db.session.add(stu)
        db.session.commit()
        return '创建学生信息成功'


@blue.route('/add_many_stu/', methods=['GET'])
def add_many_stu():
    if request.method == 'GET':
        # 批量插入学生信息
        names = ['张三1', '李四1', '隔壁老王1', '胡歌1']
        stus = []
        for name in names:
            stu = Student()
            stu.s_name = name
            stus.append(stu)
            # db.session.add(stu)
        db.session.add_all(stus)
        db.session.commit()

        return '批量插入学生信息'


@blue.route('/del_stu/', methods=['GET'])
def del_stu():
    if request.method == 'GET':
        # 删除张三1的学生信息
        stu = Student.query.filter(Student.s_name == '张三1').first()
        # db.session.delete(stu)
        # db.session.commit()
        stu.delete()
        return '删除学生信息成功'


@blue.route('/up_stu/', methods=['GET'])
def up_stu():
    if request.method == 'GET':
        # 更新隔壁老王的年龄
        stu = Student.query.filter(Student.s_name == '隔壁老王').first()
        stu.s_age = 48
        # 修改时，db.session.add(对象)可以不写
        # db.session.add(stu)
        # db.session.commit()
        stu.save_update()
        return '修改学生信息成功'


@blue.route('/sel_stu/', methods=['GET'])
def sel_stu():
    if request.method == 'GET':
        stu = Student.query.filter(Student.s_name == '张三')
        stu = Student.query.filter_by(s_name='张三')

        # 获取第一个对象
        # 在django中查询第一个Student.objects.all().first()
        stu = Student.query.all()[0]
        stu = Student.query.first()

        # get()方法
        # 获取主键所在行的对象信息
        # get()方法能够获取到对象，则返回，获取不到对象则为空
        stu = Student.query.get(2)
        stu = Student.query.filter_by(id=2).first()
        stu = Student.query.filter(Student.id == 2).first()
        for i in stu:
            print('1234567')
            print(i)

        # 排序
        stus = Student.query.order_by('-id').all()
        stus = Student.query.order_by('id').all()

        print(stus)

        # 分页, limit 1,3
        page = 1
        stus = Student.query.all()[(page-1) * 3:page * 3]
        # offset()  limit()
        stus = Student.query.offset((page-1) * 3).limit(page * 3).all()
        print(stus)

        # gt ge lt le
        stus = Student.query.filter(Student.s_age.__gt__(30)).all()
        stus = Student.query.filter(Student.s_age <= 20).all()
        print(stus)

        # 模糊查询, like % _
        stus = Student.query.filter(Student.s_name.contains('老王')).all()
        print(stus)
        stus = Student.query.filter(Student.s_name.startswith('胡')).all()
        print(stus)
        stus = Student.query.filter(Student.s_name.endswith('1')).all()
        print(stus)
        stus = Student.query.filter(Student.s_name.like('__老%')).all()
        print(stus)

        return '查询成功'

#
# @blue.route('/')
# def index():
#     msg = Message('Hello',
#                   sender='from@example.com',
#                   recipients=['to@example.com'])
#     msg.body = 'haha'
#     msg.html = '<b>testing</b>'
#     mail.send(msg)
