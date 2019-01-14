'''
数据类型转换

int(x [,base]) 将x转换为一个整数
float(x) 将x转换成浮点数
complex(real [,imag]) 创建一个复数
str(x) 将x转换成字符串
repr(x) 将x转换成表达式字符串
eval(str) 用来计算在字符串中的有效Python表达式，并返回一个对象
tuple(s) 将序列s转换成一个元组
list(s) 将序列s转换成一个列表
set(s) 将s转换为可变集合
dict(d) 创建一个字典， d必须是一个序列(key, value)元组
frozenset(s) 转换为不可变集合
chr(x) 将整数转换成字符
unichr(x) 将整数转换为unicode字符
ord(x) 将一个字符转换为它的整数值
hex(x) 将一个整数转换为一个16进制字符串
oct(x) 将一个整数转换为一个8进制字符串

举例：
# 字符串 和 数字
10 + '20' # 报错
str(10) + '20' # 1020

10 + int('20') # 30

# 元组、列表、集合 互相转换, 转换之后生成新的对象，不修改原值
a=(10,20,30)
type(a) # <class 'tuple'>
list(a) # [10, 20, 30]
set(a) {10, 20, 30}
type(a) # <class 'tuple'> 再次验证，未修改

# 列表转字典 需要特殊的形式 列表中的元素是长度为2的元组
b=[('a','AAA'),('b', 'BBB')]
m = dict(b) # {'a': 'AAA', 'b': 'BBB'}
m['a'] # AAA
m['b'] # BBB
type(m) # <class 'dict'>

# 将字符串转换为列表
list("abc") # ['a', 'b', 'c]

# 将字符串转换为元组
tuple("abc") # ('a', 'b', 'c')

# 将一个字符转成数字
ord('a') # 97
chr(97) # 'a'

'''