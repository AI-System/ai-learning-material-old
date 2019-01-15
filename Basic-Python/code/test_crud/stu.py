# 学生信息在线管理

### 定义学生列表

stulist = [
  {'name':'zs','age':10,'classid':'01'},
  {'name':'ls','age':20,'classid':'02'},
  {'name':'ww','age':30,'classid':'03'}
]

### 获取学生信息输出函数

def showStu(list):
  if len(list) == 0 :
    print('=' * 12, '没有学员信息可以输出！', '=' * 12)
    return
  print('|{0:<5} | {1:<10} | {2:<5} | {3:<10}'.format('sid', 'name', 'age', 'classid'))
  print('-' * 40)
  for i in range(len(list)):
    print('|{0:<5} | {1:<10} | {2:<5} | {3:<10}'.format(i+1, list[i]['name'], list[i]['age'], list[i]['classid']))

### 程序初始化函数

def init():
  while True:
    print('=' * 12, '学生管理系统', '=' * 12)
    print("{0:1} {1:13} {2:15}".format(" ", "1.查看学生信息", "2.添加学员信息"))
    print("{0:1} {1:13} {2:15}".format(" ", "3.删除学生信息", "4.退出系统"))
    print('=' * 40)

    key = input('请输入对应的选择：')
    # 根据键盘值，判断并执行对应的操作
    if key == '1':
      print('=' * 12, '学生信息浏览', '=' * 14)
      showStu(stulist)
      input('按回车键继续：')
    elif key == '2': 
      print('='*12, '学生信息添加', '=' * 14)
      stu={}
      stu['name'] = input('请输入学生姓名：')
      stu['age'] = input('请输入学生年龄：')
      stu['classid'] = input('请输入班级号：')
      stulist.append(stu)
      showStu(stulist)
      input('按回车键继续：')
    elif key == '3': 
      print('='*12, '学生信息删除', '=' * 14)
      showStu(stulist)
      sid=input('请输入您要删除的学生id：')
      del stulist[int(sid) - 1]
      showStu(stulist)
      input('按回车键继续：')
    elif key == '4': 
      print('='*12, '退出系统 再见！', '=' * 14)
      break # 此处跳出循环
    else: 
      print('='*12, '无效按键', '=' * 14)

init() # 执行