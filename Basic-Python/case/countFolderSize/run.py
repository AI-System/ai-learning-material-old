from library.count import count

total = 0 # 初始化总大小
total = count(total, './test')
print('test目录的数据大小为：', str(total) + ' Bytes', ' 等于： ' + str(total / 1024), 'KB') # test目录的数据大小为： 6148 Bytes  等于： 6.00390625 KB