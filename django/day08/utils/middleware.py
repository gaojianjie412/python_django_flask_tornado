import time
import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User

# 获取处理日志的logger
logger = logging.getLogger(__name__)


class TestMiddlware1(MiddlewareMixin):

    def process_request(self, request):
        print('test1 process request')
        # 对所有的请求都进行登录状态的校验
        path = request.path
        if path in ['/user/register/', '/user/login/', '/user/my_login/']:
            # 跳过以下所有代码，直接访问路由对应的视图函数
            return None

        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            request.user = user
            return None
        except Exception as e:
            return HttpResponseRedirect(reverse('user:my_login'))


    def process_view(self, request, view_func, view_args, view_kwargs):
        print('test1 view')

    def process_response(self, request, response):
        print('test1 process response')
        return response


class TestMiddlware2(MiddlewareMixin):

    def process_request(self, request):
        print('test2 process request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('test2 view')

    def process_response(self, request, response):
        print('test2 process response')
        return response


class LoggingMiddleware(MiddlewareMixin):

    def process_request(self, request):

        request.init_time = time.time()

    def process_response(self, request, response):
        try:
            # 请求到响应之间消耗时长
            count_times = time.time() - request.init_time
            # 请求地址和请求方式
            path = request.path
            method = request.method
            # 响应的状态码和内容
            status = response.status_code
            content = response.content
            # 日志记录的信息
            message = '%s %s %s %s %s' % (path, method, status, content, count_times)
            logger.info(message)
        except Exception as e:
            logger.critical('log error: %s' % e)
        return response

