import os

cwd = os.getcwd()
print('当前路径：', cwd) # 输出了当前的绝对路径

os.chdir('..') # 改变当前路径，返回上一级
cwd = os.getcwd()
print('当前路径：', cwd) # 输出了当前的绝对路径

# 循环输出当前目录中的文件列表

clist = os.listdir()

for i in clist:
  print(i)


