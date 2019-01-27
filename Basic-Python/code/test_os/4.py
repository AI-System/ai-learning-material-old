import os

### 获取环境变量

p = os.getenv('PATH')
print(p)
print('')

### 获取当前路径 都是 .

cdir = os.curdir
print(cdir) # .

## 获取上层目录路径 都是 ..

pdir = os.pardir
print(pdir) # ..

### 获取path模块， os.path 是 os中的一个子模块，操作非常多，根据不同系统，输出不一样

pth = os.path
print(pth) # <module 'posixpath' from '/anaconda3/lib/python3.6/posixpath.py'>

### 分隔符 sep (目录与目录之间的分隔符)

print(os.sep) # unix 下的分隔符，输出为：/ 根据系统不同而不同

### name 当前系统内核名称

print(os.name) # posix 这是unix下的

### os.path 模块 详细介绍

#### abspath

print(pth.abspath('dd')) # 获取当前路径下 dd 目录的绝对路径

#### exists 判断文件是否存在

print(pth.exists('xxxx.x')) # False
print(pth.exists('4.py')) # True

### 从路径字符串中提取出关键信息 basename 文件名

file = 'a/b/c/d/e/f.txt'
print(os.path.basename(file)) # f.txt

### 从路径字符串中提取出关键信息 dirname 文件所在的目录

print(os.path.dirname(file)) # a/b/c/d/e

### 连接路径

fpth1 = 'a/b/c'
fpth2 = 'c/d/e'

print(os.path.join(fpth1, fpth2)) # a/b/c/c/d/e 注意这里的 /c/c

fpth3 = 'm/n'
fpth4 = 'q/x.txt'

print(os.path.join(fpth3, fpth4)) # m/n/q/x.txt

### 获取文件大小 以下两种方法： 备注：只能获取文件大小，不能获取目录大小 (每个操作系统都获取不了)

print(os.path.getsize('4.py'))
print(os.stat('4.py').st_size) 

### 判断是否是文件、判断是否是目录

print(os.path.isfile('4.py')) # True 是否是文件
print(os.path.isdir('4.py')) # False 是否是目录

