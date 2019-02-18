# coding=utf-8

# 导入 pymysql 模块
import pymysql

# 获取数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", db="mydb", charset="utf8")

# 创建游标对象
cursor = db.cursor()

# 定义sql语句
data = ('p3', 0, 22, 'python03')
sql = "insert into stu(name, sex, age, classid)value('%s', '%d', '%d', '%s')"%(data)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 事务提交
    db.commit()
    print('成功添加条数：', cursor.rowcount)
except Exception as err:
    # 执行出错，事务回滚
    db.rollback()
    print('SQL执行错误!', err)

# 关闭数据库连接
db.close()
