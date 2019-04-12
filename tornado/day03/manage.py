import os

import tornado.web
import tornado.ioloop
from tornado.options import options, define, parse_command_line

from app.views import LoginHandler, ChatHandler

define('port', default=8081, type=int)


def make_app():
    return tornado.web.Application(handlers=[
        (r'/login/', LoginHandler),
        (r'/chat/', ChatHandler)
    ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
    static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
    cookie_secret='afsfoq2=pr24-22m3'
    )


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
