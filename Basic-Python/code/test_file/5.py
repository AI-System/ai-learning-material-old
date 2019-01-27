# 写操作

f = open('./d.txt', 'a') # a 是追加写
# 一次一次写
f.write('Hello d1\n')
f.write('Hello d2\n')

# 批量写
a = ['Hello d3\n', 'Hello d4\n', 'Hello d5\n']
f.writelines(a)

f.close()

### 执行两次 python 5.py