# coding=utf-8

# 导入 pymysql 模块
import pymysql

# 获取数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", db="mydb", charset="utf8")


# 创建游标对象
cursor = db.cursor()

# 定义sql语句
sql = 'select * from stu'

# 执行sql语句
try:
    cursor.execute(sql)
    while True:
        data = cursor.fetchone()
        if data == None:
            break
        print(data)
except:
    print('SQL执行错误!')

# 关闭数据库连接
db.close()
