'''
字典是一个非常有用的内置数据类型
列表是有序的，字典是无序的对象集合。区别：字典当中的元素是通过键存取，而不是通过下标存取
字典是一种映射类型，用 {} 标识， 它是一个无序的键值对集合
键必须使用不可变类型、在同一个字典中，键必须是唯一的。
字典有一些内置的功能函数，如：clear()、keys()、values() 等
注意：
1. 字典是一种映射类型，它的元素是键值对。
2. 创建空字典使用 {}

举例：

stu={'name':'jack', 'age': 20, 'sex': 'man'}
type(stu) # <class 'dict'>

print(stu['name']) # jack
stu['phone']='123' # 修改或添加
print(stu) # {'name':'jack', 'age': 20, 'sex': 'man', 'phone': '123'}

print(stu.keys()) # dict_keys(['name','age','sex','phone'])
print(stu.values()) # dict_values(['jack, 20, 'man', '123])

# 空的花括号默认代表字典
a={}
type(a) # <class 'dict'>

a={1,3,2}
type(a) # <class 'set'>

a={'k':1}
type(a) # <class 'dict'>

# 还可用如下三种方式初始化

b=dict.fromkeys(('a','b','c'), 100) 
b # {'a': 100, 'b': 100, 'c': 100}

d=dict.fromkeys(['a','b','c'], 100) 
d # {'a': 100, 'b': 100, 'c': 100}

e=dict.fromkeys({'a','b','c'}, 100) 
e # {'a': 100, 'b': 100, 'c': 100}

'''

### 字典的创建方式

'''
a={}
b=dict()
type(a) # <class 'dict'>
type(b) # <class 'dict'>
'''

### 删除某个key del

'''
a={'age':1, 'name': 'J'}
del a['age'] # 如果删除不存在的则会报错, 用下面的方式，删除前先做判断
a # {'name': 'J'}

# 或者用 get的方式
if 'name' in a:
  del a['name']

a # {}
'''

### 遍历字典，单项是key

'''
b={'name':'J', 'age':10, 'color':'black'}

for k in b:
  print(k, ' => ', b[k]) # 输出 key => vlaue 的形式
'''

'''
name  =>  J
age  =>  10
color  =>  black
'''

### 使用 items() 函数返回的对象来遍历 key和value

'''
b={'name':'J', 'age':10, 'color':'black'}

for k,v in b.items():
  print(k, ' => ', v)

'''

'''
name  =>  J
age  =>  10
color  =>  black
'''

### 字典内涵和字典表达式

'''
b={'name':'J', 'age':10, 'color':'black'}
a={k:v for k,v in b.items()} # 循环组装新的字典
a # {'name': 'J', 'age': 10, 'color': 'black'}

c={'name':'J', 'age':10, 'color':'black'}
d={k:v for k,v in c.items() if k=='age' or k == 'name'} # 循环组装新的字典
d # {'name': 'J', 'age': 10}
'''

### 字典函数

'''
# 字典清空
a={'name': 'J'}
a.clear()
a # {}
'''


'''
# 字典浅复制
a={'age': 10}
b=a.copy()
b # {'age': 10}
'''

'''
# 获取字典中的属性
a={'name': 'J'}
a.get('name') # J
a.get('age') # 没有的话不会报错
a.get('age', 20) # 如果没有，还可以给一个默认值 20
'''

'''
# 使用keys获取字典中的所有key
# 使用values获取字典中的所有value
a={'name': 'J', 'age': 10}
a.keys() # dict_keys(['name', 'age'])
a.values() # dict_values(['J', 10])
'''

# 批量修改字典中的值 update 有则修改，无则添加
a={'name': 'J', 'age': 10}
a.update({'age':25, 'name':'Q', 'tel': 23232})
a # {'name': 'Q', 'age': 25, 'tel': 23232}

# 删除某一个元素
a = {'age':25, 'name':'Q', 'tel': 23232}
a.pop('age')
a # {'name': 'Q', 'tel': 23232}

# 随机删除某个元素
a = {'age':25, 'name':'Q', 'tel': 23232}
a.popitem() # ('tel', 23232) 随机删除一个，返回被删除的key、vlue组成的元组
a # {'age': 25, 'name': 'Q'}