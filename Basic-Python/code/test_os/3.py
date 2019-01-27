### 查看文件状态

import os

info = os.stat('1.py')
print(info) # 返回一个元组组成的文件属性
print()
print(info.st_size) # 获取文件的大小
