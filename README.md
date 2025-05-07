# 若是第一次启动（开发时笔记，可忽略）
cd ca-backend
python -m venv venv
安装flask并输出依赖项
pip install flask flask-cors flask-sqlalchemy
pip freeze > requirements.txt
然后启动后端
python app.py


再切换到前端
cd .
cd ca-frontend
安装
npm install axios
然后启动前端
npm run dev

# 若不是首次启动
确保当前终端位于当前项目根目录
在当前终端，复制粘贴以下内容并输入
cd ca-backend
python -m venv venv
python app.py

然后重新开一个终端，复制粘贴一下内容并输入
cd ca-frontend
npm run dev


# 关于账号密码
如果想查看账号密码：信息是存储在/ca-backend/instance/site.db文件里面的
（我们使用了SQLite）
想要查看要
开启一个新的终端
cd ca-backend
打开Sqlite
sqlite3 instance/site.db  
	
	想要查询有哪些表输入：
		.table
		（输入后会显示User表，里面存储了所有账号密码用于login页面登录）
	
	想要查询User的账号密码：
		SELECT * FROM User;
