
from django.http import HttpResponseRedirect
from django.urls import reverse
# 装饰器，闭包

# 1. 外层函数内嵌内层函数
# 2. 外层函数返回内层函数
# 3. 内层函数调用外层函数的参数


def is_login(func):
    def check_status(request):
        if request.session.get('user_id'):
            return func(request)  # hindex()
        else:
            return HttpResponseRedirect(reverse('user:my_login'))
    return check_status


