
from django.urls import path, re_path

from app import views

urlpatterns = [
    # 127.0.0.1:8080/app/index/
    # re_path('index/(\d+)/', views.index),
    path('index/<int:id>/',views.index, name='index'),
    path('name/<str:name>/', views.get_name),
    # path('float/<float:uid>/', views.get_float),  # 没有float类型
    path('get_uuid/', views.get_uuid),
    path('uuid/<uuid:uid>/', views.g_uuid),
    path('path/<path:path>/', views.get_path),

    # 接收多个参数
    path('params/<int:year>/<int:month>/<int:day>/', views.params),
    # re_path('params/(\d+)/(\d+)/(\d+)/', views.params)
    # re_path('params/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.params)

    path('hindex/', views.hindex),

    # 查询所有学生列表信息
    path('all_stu/', views.all_stu, name='all_stu'),
    # 保存学生的信息
    path('add_stu/', views.add_stu, name='add_stu'),

    # 保存学生信息2
    path('add_stu_info/', views.add_stu_info, name='add_stu_info'),
    # 删除学生信息
    path('del_stu/<int:id>/', views.del_stu, name='del_stu'),

]