
import sys

from flask import Flask


# 生成flask对象，传入__name__参数，表示模块名或包名
app = Flask(__name__)


# 告诉服务器，访问127.0.0.1:5000/hello/地址可触发hello()方法
# 类似与Django中的urls.py文件的功能
@app.route('/hello/')
def hello():
    return 'hell world'


# 直接启动本文件，才执行app.run()
if __name__ == '__main__':
    # sys.argv接收启动命令时的参数，如python hello.py 0.0.0.0 80
    ip = sys.argv[1]
    port = sys.argv[2]
    # host 代表启动的ip地址
    # port 代表启动的端口
    # debug代表启动的模式，调试模型
    app.run(host=ip, port=port, debug=True)
