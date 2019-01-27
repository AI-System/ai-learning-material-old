# 复制文件功能

def copyFun(src, target):
  # src 是源文件 target是目标文件
  # 打开源文件
  f1 = open(src, 'r')
  f2 = open(target, 'w')

  # 循环读取写入
  content = f1.readline()
  while len(content) > 0:
    print(content, end="")
    f2.write(content)
    content = f1.readline()

  # 关闭源和目标文件
  f1.close()
  f2.close()

copyFun('d.txt', 'd_copy.txt')

