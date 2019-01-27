import os
import time

### 重命名 目录
os.mkdir('bb') # 创建 bb目录
os.rename('bb', 'cc') # 将bb目录重命名为cc
os.rename('cc', 'dd') # 将cc目录重命名为dd

### 重命名 文件

open('test.txt', 'w') # 创建一个test.txt文件
os.rename('test.txt', 'test1.txt') # 重命名为：test1.txt

### 删除一个目录

os.mkdir('xx') # 创建 bb目录
time.sleep(1) # 延迟一秒
os.rmdir('xx') # 删除 # 注意此处 rmdir 只能删除空目录