from flask import Flask
import config
import sys
print(sys.path)
import os
print(os.getcwd())
sys.path.insert(0,os.getcwd())
from exts import db, mail
from flask_migrate import Migrate
from blueprints.test import bp as test_bp

app = Flask(__name__)
# 连接蓝图
app.register_blueprint(test_bp)

# 绑定配置文件
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

# flask db init：只需要执行一次
# flask db migrate：将orm模型生成迁移脚本
# flask db upgrade：将迁移脚本映射到数据库中


if __name__ == '__main__':
    app.run()
