import os
import uuid
from threading import Thread

from flask import Blueprint, render_template, request, redirect, url_for
from flask_mail import Message
from sqlalchemy import and_, or_, not_


from app.models import Student, db, Grade, Course

# from manage import mail, app

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
        # for i in stu:
        #     print('1234567')
        #     print(i)

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

        # 组合查询，查询姓名中包含‘歌’，且年龄大于20
        stus = Student.query.filter(Student.s_name.contains('歌')).filter(Student.s_age > 20).all()
        stus = Student.query.filter(Student.s_name.contains('歌'), Student.s_age >= 20).all()
        # 且 and_:默认就是且的操作，可以不写
        stus = Student.query.filter(and_(Student.s_name.contains('歌'), Student.s_age >= 20)).all()

        # 或 or_
        stus = Student.query.filter(or_(Student.s_name.contains('歌'), Student.s_age <= 20)).all()
        # 非 not_
        stus = Student.query.filter(not_(Student.s_name.contains('歌')), Student.s_age > 30).all()

        print(stus)

        return '查询成功'


# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# @app.route('/')
# def index():
#     msg = Message(subject='Hello',
#                   sender='',
#                   recipients=['947147944@qq.com'])
#     msg.body = '猜猜我是谁'
#     msg.html = '<b>testing</b>'
#     mail.send(msg)
#     thread = Thread(target=send_async_email, args=[app, msg])
#     thread.start()
#     return '<h1>邮件发送成功</h1>'


@blue.route('/all_stu/', methods=['GET'])
def all_stu():
    if request.method == 'GET':
        # 从url中获取page参数
        page = int(request.args.get('page', 1))
        # stus是分页的对象
        pg = Student.query.paginate(page, 3)
        # 获取当页的数据
        stus = pg.items
        return render_template('stus.html', stus=stus, pg=pg)


@blue.route('/add_grade/', methods=['GET'])
def add_grade():
    if request.method == 'GET':
        gnames = ['Python', 'Java', 'Php', 'C++', 'C']
        for name in gnames:
            g = Grade()
            g.g_name = name
            db.session.add(g)
        db.session.commit()

        return '创建班级成功'


@blue.route('/create_stu_grade/', methods=['GET'])
def create_stu_grade():
    if request.method == 'GET':
        # 获取id为1和2的两个学生
        stu1 = Student.query.get(1)
        stu2 = Student.query.get(2)
        # 分配给python班级
        g = Grade.query.filter(Grade.g_name == 'Python').first()
        stu1.g_id = g.id
        stu1.save_update()

        stu2.g_id = g.id
        stu2.save_update()

        return '分配学生成功'


@blue.route('/sel_stu_by_grade/', methods=['GET'])
def sel_stu_by_grade():
    if request.method == 'GET':
        grade = Grade.query.filter_by(g_name='Python').first()
        # 通过班级对象查询该班级下的学生信息
        # stus是列表
        stus = grade.s_g
        stus_name = [stu.s_name for stu in stus]

        return '该班级下学生的姓名为：%s ' % stus_name


@blue.route('/sel_grade_by_stu/', methods=['GET'])
def sel_grade_by_stu():
    if request.method == 'GET':
        stu = Student.query.filter(Student.s_name == '张三').first()
        # 通过学生查询班级
        grade = stu.g

        return '张三属于%s班级' % grade.g_name


@blue.route('/add_course/', methods=['GET'])
def add_course():
    if request.method == 'GET':
        courses = ['语文', '数学', '英语', '物理', '化学', '生物', '普通地质学', '构造地质学']
        # for course in courses:
        #     c = Course()
        #     c.c_name = course
        #     db.session.add(c)
        # db.session.commit()
        c = []
        for course in courses:
            cou = Course()
            cou.c_name = course
            c.append(cou)
        db.session.add_all(c)
        db.session.commit()

        return '创建课程成功'


@blue.route('/stu_cou/', methods=['GET'])
def stu_cou():
    if request.method == 'GET':
        # 给胡歌添加英语和物理的课程
        stu = Student.query.filter(Student.s_name == '胡歌').first()
        stu1 = Student.query.filter(Student.s_name == '隔壁老王').first()

        cou1 = Course.query.filter(Course.c_name == '英语').first()
        cou2 = Course.query.filter(Course.c_name == '物理').first()
        # 添加
        # stu.cou.append(cou1)
        # stu.cou.append(cou2)

        # cou1.stu.append(stu1)
        # 删除
        stu.cou.remove(cou1)

        db.session.commit()
        return '添加学生课程成功'


@blue.route('/edit_stu/<int:id>/', methods=['GET', 'POST'])
def edit_stu(id):
    if request.method == 'GET':
        stu = Student.query.get(id)
        return render_template('edit.html', stu=stu)
    if request.method == 'POST':
        # 接收图片，并保存图片
        icon = request.files.get('image')
        # 获取媒体文件的路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        STATIC_DIR = os.path.join(BASE_DIR, 'static')
        MEDIA_DIR = os.path.join(STATIC_DIR, 'media')
        # 随机生成图片的名称
        filename = str(uuid.uuid4())
        a = icon.mimetype.split('/')[-1:][0]
        name = filename + '.' + a
        # 拼接图片的地址和名称
        path = os.path.join(MEDIA_DIR, name)
        # 保存
        icon.save(path)
        # 修改用户的头像icon字段
        stu = Student.query.get(id)
        stu.icon = name
        stu.save_update()

        # 重定向到列表页面
        return redirect(url_for('app.all_stu'))
