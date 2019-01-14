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