import os

def count(total, path):
  '''定义统计文件夹功能'''
  dlist = os.listdir(path) # 获取当前路径下的文件列表
  # 循环文件列表的
  for f in dlist:
    # 为遍历的文件添加目录路径
    file = os.path.join(path, f) # 拼合文件路径
    # 判断是否是文件
    if os.path.isfile(file):
      # 注：此处有两种获取文件大小的方式 os.path.getsize(file) 和 os.stat(file).st_size
      total += os.path.getsize(file)
    ## 判断是否是目录
    if os.path.isdir(file):
      count(total, file) # 递归
  return total