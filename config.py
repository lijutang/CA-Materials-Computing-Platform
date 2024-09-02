# config.py 用于保存配置信息
SECRET_KEY = "xxxxx"

# 数据库的配置信息
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "database_cas"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "xxx@qq.com"
MAIL_PASSWORD = "xxxxx"
MAIL_DEFAULT_SENDER = "xxx@qq.com"