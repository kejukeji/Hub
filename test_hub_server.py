# coding: UTF-8

# 设置python运行环境的编码
from flask import render_template
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask

# from models import db
# from .ex_var import CONFIG_FILE

# 创建应用程序入口
app = Flask(__name__)
# 加载配置文件
# app.config.from_pyfile(CONFIG_FILE)


# 关闭数据库
#@app.teardown_appcontext
#def close_data_base(exception=None):
#    if exception is not None:
#        print('+++++++' + str(exception) + '+++++++')
#
#    if db is not None:
#        db.remove()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7557)


#@app.teardown_request
#def teardown_request(exception=None):
#    if db is not None:
#        db.remove()
#
#import urls