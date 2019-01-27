# 一次性读取所有行

f = open('./a.txt', 'r')
content = f.readline()

flist = f.readlines()

for line in flist:
  print(line,end="")

f.close()