import os

import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from face.views import RegisterHandler, InitdbHandler, LoginHandler

define('port', default=8081, type=int)


def make_app():
    return tornado.web.Application(handlers=[
        (r'/register/', RegisterHandler),
        (r'/init_db/', InitdbHandler),
        (r'/login/', LoginHandler),
    ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
    static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
    )


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
