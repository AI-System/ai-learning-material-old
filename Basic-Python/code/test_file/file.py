### 简单读取

'''
### r模式下, 文件光标在开头; w 模式是清空写模式; a 模式追加 光标在最后，

f = open('./a.txt', 'r')

### 读取文件内容并输出
content = f.read(5) # 如果不写参数，则是一口气读完
print(content) # Hello
### 关闭
f.close()

'''

### readline() 读取一行 适用于读取大文件

'''
f=open('./a.txt', 'r')
content = f.readline()
while len(content) > 0:
  content = f.readline()
  print(content, end="")
f.close()
'''

### 读取所有的行 readlines 试用于读取小文件

'''
f=open('./a.txt', 'r')
flist = f.readlines() # 返回一个列表

for line in flist:
  print(line, end="")

f.close()
'''

### 简单的文件写入操作

'''
f=open('./b.txt', 'w') # 清空写
f.write('Hello Java\n')
f.write('Hello Java\n')
f.close()
'''

### 批量写

'''
a=['Hello World\n', 'Hello Java\n', 'Hello Python\n']
f=open('./b.txt', 'w') # w是清空写，a是追加写
f.writelines(a)
f.close()
'''

### 自定义文件复制函数

def myCopy(file1, file2):
  '''
  file1 : 源文件
  file2 : 目标文件
  '''
  # 1. 打开两个文件
  f1 = open(file1, 'r')
  f2 = open(file2, 'w')
  # 2. 循环读取并写入实现复制内容
  content = f1.readline()
  while len(content) > 0:
    f2.write(content)
    content = f1.readline()
  # 3. 关闭两个文件
  f1.close()
  f2.close()

# myCopy('./a.txt', './a_copy.txt') 

### 关于图片，声音，视频，可执行程序等二进制文件读取
'''
需要注意的是二进制文件读取时，模式要选择相应的b 如 rb

文档内容一般分为2种格式：
1. 字符(一般不需要处理)
2. 字节(二进制)

二进制的需要特殊处理：
f1 = open(file1, 'rb')
f2 = open(file2, 'wb')

此处不再举例
'''

### 目录操作 

'''
import os
os.getcwd() # 获取当前工作目录
os.chdir('your dir') # 跳转到某个目录
os.listdir() # 列出当前目录下的文件 返回一个文件列表

举例：
a = os.listdir()
for i in a:
  print(i)

os.mkdir('bb') # 创建一个目录
os.rename('bb', 'cc') # 把 bb 文件/文件夹 改名为 cc
os.rmdir('cc') # 删除 cc 的文件夹 适合 空文件
os.rmdir('aa') # 如果aa目录中有文件，则会报错
os.stat('file.py') # 返回一个文件对象

举例：

info=os.stat('file.py')
info.st_size # 获取文件大小
info.其他属性 # 获取其他属性信息

系统命令

os.getenv('PATH') # 获取环境变量
os.putenv()
os.exit() 退出当前执行命令，直接关闭当前操作
os.system() 执行系统命令
'''

### 当前os模块的值

'''
os.curdir # 获取当前目录
os.name # 获取当前是什么系统
os.sep # 获取当前系统的分隔符 windows下是 \\  linux下是 / 常用，便于程序的移植性
os.extsep # 获取当前系统中文件名和后缀之间的分隔符号，所有系统都是 不常用
os.linesep # 获取当前系统的换行符号 不常用

### os.path 模块

os.path.abspath('相对路径') # 将相对路径转换为绝对路径
os.path.basename('路径') # 获取路径中文件夹或文件名称
os.path.dirname('路径') # 获取路径中的路径部分
os.path.join('路径1','路径2') # 将2个路径合成1个路径
os.path.split('路径') # 将一个领切割成文件夹和文件名部分
os.path.splitext('文件名称') # 将一个文佳宁切成名字和后缀两个部分 返回值 元组(名称,后缀)
os.path.getsize('路径') # 获取一个文件的大小 返回值 整数 只能是文件大小，不是目录大小 获取目录大小需要遍历
os.path.isfile('路径') # 检测一个路径是否是一个文件 返回值 布尔
os.path.exists('路径') # 检测文件是否存在 返回值 布尔

'''

### 复制文件夹的函数

'''
import os

def myCopy(file1, file2):
  '''
  file1 : 源文件
  file2 : 目标文件
  '''
  # 1. 打开两个文件
  f1 = open(file1, 'r')
  f2 = open(file2, 'w')
  # 2. 循环读取并写入实现复制内容
  content = f1.readline()
  while len(content) > 0:
    f2.write(content)
    content = f1.readline()
  # 3. 关闭两个文件
  f1.close()
  f2.close()


def copyDir(dir1, dir2):
  # 获取被复制目录中的所有文件信息
  dlist = os.listdir(dir1)
  # 创建新的目录
  os.mkdir(dir2)
  # 遍历所有文件，并执行文件复制
  for f in dlist:
    # 为遍历的文件添加目录路径
    file1 = os.path.join(dir1, f) # 源
    file2 = os.path.join(dir2, f) # 目标
    # 判断是否是文件
    if os.path.isfile(file1):
      myCopy(file1, file2) # 调用自定义文件复制函数来复制文件
    ## 判断是否是目录
    if os.path.isdir(file1):
      copyDir(file1, file2) # 递归调用自己，来实现子目录的复制

'''

### todo 使用文件和目录操作，定义一个递归统计目录大小的函数

'''
^_^
'''