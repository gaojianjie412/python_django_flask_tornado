import tornado.web
import tornado.websocket

class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        error = ''
        self.render('login.html', error=error)

    def post(self):
        # 获取登录用户信息
        username = self.get_argument('username')
        password = self.get_body_argument('password')
        # 模拟登录，校验功能
        if username in ['coco', 'vincent', '哈哈'] and password == '123456':
            self.set_secure_cookie('username', username)
            self.render('chat.html', username=username)

        else:
            error = '账户或者密码输入错误，请重新输入'
            self.render('login.html', error=error)


class ChatHandler(tornado.websocket.WebSocketHandler):
    # 用于存放连接对象
    user_online = []

    def open(self, *args, **kwargs):
        self.user_online.append(self)
        for user in self.user_online:
            # 当进入chat.html页面时，会主动触发该函数
            username = self.get_secure_cookie('username').decode('utf-8')
            user.write_message('系统提示：【%s已进入聊天室】' % username)

    def on_message(self, message):
        # 接收前端传的数据
        username = self.get_secure_cookie('username').decode('utf-8')
        for user in self.user_online:
            user.write_message('%s:%s' % (username, message))

    def on_close(self):
        # 移除连接对象
        self.user_online.remove(self)
        for user in self.user_online:
            username = self.get_secure_cookie('username').decode('utf-8')
            user.write_message('系统提示：【%s已退出聊天室】' % username)