'''

list 可以完成大多数集合类的数据结构实现 
列表中元素类型可以不相同，支持数字、字符串、甚至可包含列表(嵌套)
索引值从0开始，-1表示从末尾开始的位置
+是列表连接运算符， * 是重复操作

举例：
a=[10,20,30] # 定义一个列表
type(a) # <class 'list'>

a[0] # 10
a[1] # 20
a[-1] # 30
a[1]=100 # 修改某一项的值
print(a) # [10,100,30]
a[1:2] # [100] 
a[1:] # [100, 30]

b=[8,9]
print(a + b) # [10,100,30,8,9]

print(b * 2) # [8,9,8,9]

'''

### 创建列表的2种方法

'''
list0=[]
list1=list()
'''

### 遍历list的方式

'''
a=[10,20,30,40,50]

for i in a:
  print(i)
'''


'''
a=[10,20,30,40,50]
i=0
while i < len(a):
  print(a[i])
  i+=1
'''

### 遍历有规律的二级列表

'''
b=[[10,20],[30,40],[50,60]]

for v1,v2 in b:
  print(v1, v2)

'''

### 遍历非等长的列表

'''
c=[[10],[20,30],[40,50,60]]

for v in c:
  for i in v:
    print(i, end=" ")
  print()
'''

'''
10
20 30
40 50 60
'''

### 判断成员

'''
in 、 not in
'''

### 列表中添加一个值 append 只能添加一个值

'''
a=[1,2,3]
a.append(4)
a # [1, 2, 3, 4]
'''

### 列表中添加多个值

'''
a=[1,2,3]
a.extend([4,5,6])
a # [1, 2, 3, 4, 5, 6]
'''

### 列表中某个位置插入一个值

'''
a=[1,2,3]
a.insert(2, 'bb') # 在第三个位置上加上一个值
a # [1, 2, 'bb', 3]
'''

### 列表中的统计某个元素出现的次数

'''
a=[1,2,2,3]
a.count(2) # 2
'''

### 查找某个元素

'''
a=[1,2,2,3]
a.index(2) # 1
a.index(3) # 3
'''

### 弹出某个元素

'''
a=[1,2,3,4]
res = a.pop(2) # 删除索引为2的元素: 3
res # 3
a # [1, 2, 4]
'''

### 删除某个元素

'''
a=['aa','bb','cc','dd']
a.remove('cc') # 删除 cc 不返回 任何东西
a # ['aa', 'bb', 'dd']
'''

### 逆转列表元素的顺序

'''
a=[1,2,3,4]
a.reverse() # 逆转 不返回任何东西
a # [4, 3, 2, 1]
'''

### 列表排序， 需要统一数据类型的才可以排序

'''
a=[8,9,10,11,5,0]
a.sort() # 排序 ， 此表达式不返回任何操作
a # [0, 5, 8, 9, 10, 11]
'''

### 列表复制

'''
a=[1,2,3]
b=a.copy()
a # [1, 2, 3]
b # [1, 2, 3]
id(a) == id(b) # False 拷贝之后形成一个新的对象
'''

### 清理列表 clear

'''
a=[1,22,33]
a.clear() # 清理
a # []
'''

### 获取列表中最大值和最小值

'''
a = [1,2,3,4]
min(a) # 1
max(a) # 4
'''
