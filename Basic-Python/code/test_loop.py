# while 循环

### 循环输出 1~10

'''
i=1
while i<=10:
  print(i) # 循环的内容
  i+=1 
'''
### 倒着循环输出 1~10

'''
i=10
while i>=1:
  print(i, end=" ") # end 参数不换行
  i-=1
'''

### 计算 1 ~ 100 的累加操作

'''
i=1
sum=0
while i<=100:
  sum+=i
  i+=1
print(sum) # 5050
'''

### 死循环的使用

while True:
  k=input('请输入值：')
  print('内容：', k)
  # 跳出死循环
  if k=='q':
    print('跳出了循环，谢谢！')
    break
