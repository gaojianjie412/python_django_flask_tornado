
import uuid

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import Student


def index(request, id):
    print(type(id))
    name = '小明'
    a = [89, 76, 46, 98, 100]
    content_h2 = '<h2>天气真好</h2>'
    return render(request,
                  'index.html',
                  {'name': name, 'a': a, 'b': content_h2}
                  )


def get_name(request, name):
    print(type(name))
    return HttpResponse('name:%s' % name)


def get_float(request, num):
    return HttpResponse('float number:%s' % num)


def get_uuid(request):
    uid = str(uuid.uuid4())
    return HttpResponse(uid)


def g_uuid(request, uid):
    return HttpResponse('uuid:%s' % uid)


def get_path(request, path):
    return HttpResponse('path: %s' % path)


def params(request, month, day, year):
    return HttpResponse('%s年%s月%s日' % (year, month, day))


def hindex(request):
    if request.method == 'GET':
        # return HttpResponse('HELLO WORLD')
        # return render()
        # return JsonResponse({'code': 200, 'msg': '请求成功'})
        # return HttpResponseRedirect('/app/index/1/')
        return HttpResponseRedirect(
            reverse('app:index', kwargs={'id': 2})
        )

    if request.method == 'POST':
        pass


def all_stu(request):
    if request.method == 'GET':
        # 获取分页的脚码
        page = int(request.GET.get('page', 1))
        # 第一种方式： 使用切片实现分页
        # stus = Student.objects.all()[((page-1) * 3):(page * 3)]
        # 第二种方式: 使用Paginator库实现分页
        stus = Student.objects.all()
        pg = Paginator(stus, 3)
        stus = pg.page(page)
        return render(request, 'stus.html', {'stus': stus})


def add_stu(request):
    if request.method == 'GET':
        return render(request, 'add_stus.html')

    if request.method == 'POST':
        # 1. 获取数据
        username = request.POST.get('username')
        icon = request.FILES.get('icon')
        # 2. 保存
        Student.objects.create(s_name=username,
                               icon=icon)
        # 3. 跳转到列表页面
        return HttpResponseRedirect(reverse('app:all_stu'))
