'''

Python3 中有6个标准的数据类型
1. Number(数字)
2. String(字符串)
3. List(列表)
4. Tuple(元组)
5. Sets(集合)
6. Dictionary(字典)

'''

'''
1. Number 数值类型

Python3 支持 int、float、 bool、complex(复数)
在Python3 中，只有一种整数类型 int, 表示长整型，没有python2中的Long
内置 type 函数可查询变量的类型
还可用 isinstance 来判断

注： 在python2 中没有布尔类型、用0标识False、用1表示True
在python3 中把True和False定义成关键字，但他们的值还是1和0，可以和数字运算
可以通过del语句和是哪出单个或多个对象： del var1,var2

举例：

a=10
type(a) # <class 'int'>

b=2.5
type(b) # <class 'float'>

c=True
type(c) # <class 'bool'>

c=False
type(c) # <class 'bool'>

d=4+3j
type(d) # <class 'complex'>

isinstance(a, int) # True
isinstance(a, float) # False

'''
