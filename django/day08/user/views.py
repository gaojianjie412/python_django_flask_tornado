import random

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from app.models import Student
from user.models import User, UserToken
from user.serializers import StuSerializer
from utils.functions import is_login


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 获取登录提交的参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        # 校验密码
        if check_password(password, user.password):
        # if username == 'coco' and password == '123123':
            # 模拟登陆成功, 跳转到首页
            # 设置cookie
            res = HttpResponseRedirect(reverse('user:index'))
            s = '1234567890qwertyuiopasdfghjklzxcvbnm'
            token = ''
            for i in range(20):
                token += random.choice(s)
            res.set_cookie('token', token, max_age=30)
            # 保存token到user_token表中
            UserToken.objects.create(user_id=user.id, token=token)
            return res
        else:
            # 模拟登陆失败
            # return render(request, 'login.html')
            return HttpResponseRedirect(reverse('user:login'))


def index(request):
    if request.method == 'GET':
        # 从cookies中获取登录校验的token值
        token = request.COOKIES.get('token')
        # 判断token是否存在，如果不存在说明没有登录或登录失效
        if not token:
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        # 判断user_token表中是否存在token值，如果不存在，表示用户没有登录
        if not user_token:
            return HttpResponseRedirect(reverse('user:login'))
        return render(request, 'index.html')


def logout(request):
    if request.method == 'GET':
        res = HttpResponseRedirect(reverse('user:login'))
        # 删除cookie中的键值对
        res.delete_cookie('token')
        return res


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        # 1. 接收页面中传递的参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # 2. 实现保存用户信息到user表中
        if User.objects.filter(username=username).exists():
            msg = '账号已存在'
            return render(request, 'register.html', {'msg': msg})
        if password != password2:
            msg = '密码不一致'
            return render(request, 'register.html', {'msg': msg})
        password = make_password(password)
        User.objects.create(username=username, password=password)
        # 3. 跳转到登录
        return HttpResponseRedirect(reverse('user:login'))
        # return render(request, 'login.html')


def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if check_password(password, user.password):
            # 1. 向cookie中保存键值对，键为sessionid
            # 2. 向django_session表中存sessionid值
            # 3. 向django_session表中存储键值对{‘username’: coco}
            # request.session['username'] = username
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('user:hindex'))
        else:
            msg = '账号或密码错误'
            return render(request, 'login.html', {'msg': msg})

#
# def hindex(request):
#     if request.method == 'GET':
#         if request.session.get('user_id'):
#             user_id = request.session['user_id']
#             user = User.objects.get(pk=user_id)
#             print('当前登录系统的人为:%s' % user.username)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html')



def hindex(request):
    if request.method == 'GET':
        print('index')
        return render(request, 'index.html')



def my_logout(request):
    if request.method == 'GET':
        # 1. 删除cookie中的sessionid值
        # 2. 删除django_session表中的数据
        # 3. 删除django_session中session_data中的user_id
        # request.session.flush()
        del request.session['user_id']
        return HttpResponseRedirect(reverse('user:my_login'))


class StuView(viewsets.GenericViewSet,
              mixins.ListModelMixin,  # 查看所有资源   GET
              mixins.RetrieveModelMixin,  # 查看指定id的资源  GET
              mixins.DestroyModelMixin,   # 删除指定的资源   DELETE
              mixins.CreateModelMixin,    # 创建资源   POST
              mixins.UpdateModelMixin):   # 修改资源   PUT/PATCH
    # 指定资源返回的内容
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(is_delete=0)
    # 序列化queryset的结果
    serializer_class = StuSerializer

    # 查询所有信息时，过滤掉被删除的学生信息
    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(is_delete=0)

    def perform_destroy(self, instance):
        instance.is_delete=1
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Exception as e:
            return Response({'code': 404, 'msg': '获取失败', 'data':''})


def stu_list(request):
    if request.method == 'GET':
        return render(request, 'stu_list.html')