from library.count import count

total = 0 # 初始化总大小
total = count(total, './test')
print('test目录的数据大小为：', str(total) + ' Bytes', ' 等于： ' + str(total / 1024), 'KB') # test目录的数据大小为： 28008 Bytes  等于： 27.3515625 KB