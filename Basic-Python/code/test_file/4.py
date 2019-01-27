# 写操作

f = open('./c.txt', 'w') # w 是清空写
# 一次一次写
f.write('Hello c1\n')
f.write('Hello c2\n')

# 批量写
a = ['Hello c3\n', 'Hello c4\n', 'Hello c5\n']
f.writelines(a)

f.close()