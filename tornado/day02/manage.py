import os

import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from app.views import IndexHandler, XindexHandler, DbHandler, DropHandler, AddStuHandler, StusHandler

# 设置默认端口
define('port', default=80, type=int)


def make_app():
    return tornado.web.Application(handlers=[
        (r'/', IndexHandler),
        (r'/xindex/', XindexHandler),
        (r'/init_db/', DbHandler),
        (r'/drop_db/', DropHandler),
        (r'/add_stu/', AddStuHandler),
        (r'/stus/', StusHandler),
    ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
    static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    )


if __name__ == '__main__':
    # 解析命令行
    parse_command_line()
    # 生成Application对象
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 启动
    tornado.ioloop.IOLoop.current().start()