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

'''
