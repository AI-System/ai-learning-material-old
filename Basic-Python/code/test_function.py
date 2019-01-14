'''

函数的本质是功能的封装 使函数大大提高编程效率与程序的可读性

函数能够实现特定功能的计算机代码而已，他是一种特定的代码组结构。

函数的作用：
1. 提升代码重复利用率，避免重复开发相同的代码
2. 提高开发效率
3. 便于程序维护

定义函数的规则
1. 函数代码块以 def 关键字开头，后接函数标识符名称和圆括号()
2. 任何传入参数和自变量必须放在圆括号内，圆括号之间可以用于定义参数
3. 函数第一行语句可以选择性地使用文档字符串以用于存放函数的说明
4. 函数内容以冒号起始， 并且缩进
5. return 结束函数，选择性地返回一个值给调用方， 不带表达式的return 相当于返回 None

函数的定义格式

1. 基本函数格式
2. 带有参数的函数格式
3. 带有默认值的参数
4. 关键字参数
5. 收集参数(带*)
6. 多种参数混合


'''

'''
# 基本的定义
def aa():
  print('111')
  print('222')
  print('333')

aa() # 调用
'''

### 含有参数的函数

'''
def bb(m1, m2):
  print(m1 + m2)

bb()
'''

### 带有默认值的函数

'''
def cc(name='jack', age=20, sex='man'):
  print(name)
  print(age)
  print(sex)

cc() # 不传递参数 用默认值
cc('John') # 只传递一个
cc('Lily', 18, 'female') 传递参数，用参数
'''

### 关键字参数 可以改变传递顺序

'''
def dd(name='jack', age=20, sex='man'):
  print(name)
  print(age)
  print(sex)

# 可以有效防止参数传错
dd(sex="female", age=10, name="JJ") # 参数不通过参数的位置来决定，通过参数对应的关键字属性决定，不用考虑传递顺序
'''

### 收集参数

#### 非关键字收集 

'''
def demo(*arg):
  print(arg) # 以元组的方式 得到参数
  sum=0
  for i in arg:
    sum+=i
  print('final sum: ', sum)

demo(10, 20, 30)
'''

#### 关键字收集 注意用 2颗* 

'''
def demo(**arg):
  print(arg) 

demo(name="jack", age=10) # 调用后输出的是字典参数 输出：{'name':'jack', 'age':10}

'''

### 混合模式

'''
def demo(m, **arg):
  print(m)
  print(arg)

demo(10, name="jack", age=10) # 调用后输出的是字典参数 输出：10, {'name':'jack', 'age':10}
'''

### 返回值的使用

#### 定义一个计算指定数值累加的函数

'''
def sum(m):
  # 在内部写注释
  total=0
  for i in range(0, m+1):
    total += i
  return total

print(sum(100)) # 5050
'''


#### 两种方式查看文档函数

'''
help(sum) # 在终端下输出
sum.__doc__ # 在文档输出
'''

#### 局部变量和全局变量

'''
1. 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用于
2. 局部变量只能再起被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
3. 调用函数时，所有在函数内声明的变量名称都精被加入到作用域中。

'''

##### 函数外定义的称全局变量

'''
name = 'zhagnsan'

def fun():
  name='lisi'
  print(name) # 输出的是 lisi 局部变量
  

fun()
print('函数外输出全局变量： name: ', name) # 函数外输出全局变量： name:  zhagnsan
'''

##### 使用 global 使用全局变量

'''
name = 'zhagnsan'

def fun():
  global name
  print(name) # 输出的是 zhangsan
  name='lisi' # 此处修改了全局变量

fun()
print('函数外输出全局变量： name: ', name) # 函数外输出全局变量： name:  lisi
'''

### 匿名函数 lambda 表达式

'''
1. 匿名函数：即不再使用def语句这样标准的形式定义一个函数
2. python 使用 lambda 来创建匿名函数
3. lambda 只是一个表达式，函数体比def简单很多
4. lambda 主体是一个表达式，而不是代码块，仅仅能在lambda表达式中封装有限的逻辑进去。
5. lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
6. 虽然lambda函数看起来只能写一行，却不等同于c或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
7. 语法：lambda 函数的语法只包含一个语句，如：lambda [arg1, [arg2, ...argn]]:expression
'''

'''
sum=lambda v1, v2: v1+v2 # 这个方式中 冒号前面的是参数，冒号后面的是最终return出去的
print(sum(1,2)) # 3
'''