# coding=utf-8

'''
封装数据库操作实体类
'''

import pymysql
from db import config

class Model:
    ''' 单表信息操作类 '''
    tab_name = None #表名
    link = None     #数据库连接对象
    cursor = None   #游标对象
    pk = 'id'       #主键字段名
    fields = []     #表的所有字段名

    def __init__(self, table, config=config):
        ''' 构造方法，初始化表名、通过配置参数连接数据库、创建游标对象等'''
        try:
            self.tab_name = table
            self.link = pymysql.connect(host=config.HOST,user=config.USER,password=config.PASSWD,db=config.DBNAME,charset="utf8")
            self.cursor = self.link.cursor(pymysql.cursors.DictCursor)
            # 调用内部方法，加载当前表的字段信息
            self.__loadFields()
        except Exception as err:
            print("Model初始化报错，原因：%s" % err)

    def __loadFields(self):
        sql = "SHOW COLUMNS FROM %s"%(self.tab_name)  #desc 表名
        self.cursor.execute(sql)
        vo = self.cursor.fetchall()
        #遍历所有字段信息
        for v in vo:
            self.fields.append(v['Field'])
            #判断并收集表的主键名称
            if v['Key'] == 'PRI':
                self.pk = v['Field']


    def findAll(self):
        '''获取全部功能'''
        try:
            sql = "select * from %s"%(self.tab_name)
            self.cursor.execute(sql) 
            return self.cursor.fetchall()
        except Exception as err:
            print("SQL查询执行错误，原因：%s" % err)
            return []

    def find(self,id):
        '''获取指定主键值的当条信息，没有返回None'''
        try:
            sql = "select * from %s where %s='%s'"%(self.tab_name,self.pk,id)
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as err:
            print("SQL查询执行错误，原因：%s" % err)
            return None

    def select(self,where=[],order=None,limit=None):
        '''获取当前表的所有信息，没有信息返回空列表[]'''
        try:
            sql = "select * from %s "%(self.tab_name)
            if isinstance(where,list) and len(where)>0:
                sql += " where "+" and ".join(where)
            if order is not None:
                sql += " order by "+order
            if limit is not None:
                sql += " limit "+str(limit)
            # print(sql)
            self.cursor.execute(sql) 
            return self.cursor.fetchall()
        except Exception as err:
            print("SQL查询执行错误，原因：%s" % err)
            return []

    def save(self,data={}):
        ''' 添加数据方法，通过字典参数data传递要添加的信息，并实现添加操作'''
        try:
            #组装sql语句
            keys = []
            values = []
            for k,v in data.items():
                if k in self.fields:
                    keys.append(k)
                    values.append(v)
            sql = "insert into %s(%s) values(%s)"%(self.tab_name,','.join(keys),','.join(['%s']*len(values)))
            #指定参数，并执行sql添加
            self.cursor.execute(sql,tuple(values))
            # 事务提交
            self.link.commit()
            #获取并返回最新自增ID
            return self.cursor.lastrowid
        except Exception as err:
            print("SQL添加执行错误，原因：%s" % err)
            return 0

    def update(self,data={}):
        '''修改功能'''
        try:
            values = []
            for k,v in data.items():
                if (k in self.fields) and (k != self.pk):
                    values.append("%s='%s'"%(k,v))
            sql = "update %s set %s where %s='%s'"%(self.tab_name,','.join(values),self.pk,data.get(self.pk))
            # print(sql)
            # 指定参数，并执行修改sql
            self.cursor.execute(sql)
            # 事务提交
            self.link.commit()
            #返回数据条数或影响行数
            return self.cursor.rowcount
        except Exception as err:
            print("SQL修改执行错误，原因：%s" % err)
            return 0

    def delete(self,id=0):
        '''删除功能'''
        try:
            #组装sql语句
            sql = "delete from %s where %s='%s'"%(self.tab_name,self.pk,id)
            # print(sql)
            #指定参数，并执行修改sql
            self.cursor.execute(sql)
            #事务提交
            self.link.commit()
            #返回数据条数或影响行数
            return self.cursor.rowcount
        except Exception as err:
            print("SQL修改执行错误，原因：%s" % err)
            return 0

    def __del__(self):
        #关闭游标对象
        if self.cursor != None:
            self.cursor.close()
        #关闭数据库连接
        if self.link != None:
            self.link.close()