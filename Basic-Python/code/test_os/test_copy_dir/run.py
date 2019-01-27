# 复制文件功能
import os

### 复制文件函数
def copyFun(src, target):
  # src 是源文件 target是目标文件
  # 打开源文件
  f1 = open(src, 'rb')
  f2 = open(target, 'wb')

  # 循环读取写入
  content = f1.readline()
  while len(content) > 0:
    print(content, end="")
    f2.write(content)
    content = f1.readline()

  # 关闭源和目标文件
  f1.close()
  f2.close()

### 复制目录函数
def copyDirFun(srcDir, targetDir):
  ### 1. 获取被复制目录中的所有文件信息
  dlist = os.listdir(srcDir)
  ### 2. 创建新目录
  os.mkdir(targetDir)
  ### 3. 遍历所有文件，执行文件复制
  for i in dlist:
    # 为遍历的文件添加目录路径
    file1 = os.path.join(srcDir, i) # 源文件
    file2 = os.path.join(targetDir, i) # 目标文件
    # 判断是否是文件, 是文件则复制, 是目录则递归
    if os.path.isfile(file1):
      copyFun(file1, file2) # 复制当前源目录文件到目标目录
    if os.path.isdir(file1):
      copyDirFun(file1, file2)

### 开始复制
copyDirFun('./aa', './bb')
