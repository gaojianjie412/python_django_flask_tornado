
from django.urls import path
from rest_framework.routers import SimpleRouter

from user import views
# 声明路由对象
router = SimpleRouter()
router.register('student', views.StuView)

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('my_login/',views.my_login, name='my_login'),
    path('hindex/', views.hindex, name='hindex'),
    path('my_logout/', views.my_logout, name='my_logout'),
    path('stu_list/', views.stu_list, name='stu_list'),
]

urlpatterns += router.urls
