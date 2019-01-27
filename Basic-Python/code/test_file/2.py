# 读取一行

f = open('a.txt')
content = f.readline() # 读取一行
# print(content)

# 通过循环的方式读取一行
while len(content) > 0:
  print(content, end="")
  content = f.readline() # 接着读

f.close() # 读完关闭