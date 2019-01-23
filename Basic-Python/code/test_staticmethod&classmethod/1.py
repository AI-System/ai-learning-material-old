# 最简单的调用
class A:
  def fun(self):
    print('aaaaaa')

a = A()
a.fun() # aaaaaa

print('⭐️ ' * 20)

class B:
  def fun():
    print('bbb')
  fun = staticmethod(fun) # 将fun方法设置为【静态方法】，注：静态方法无参数

  def demo(self):
    print('demo')
  demo = classmethod(demo) # 类成员方法定义 和静态方法的区别是 一个无参数，一个有参数
  
B.fun() # bbb
B.demo() # demo

### 装饰器方法

class C:
  @staticmethod
  def fun():
    print('c fun...')
  
  @classmethod
  def demo(self):
    print('c demo...')

C.fun() # c fun...
C.demo() # c demo...

### 私有属性是否存在

class D:
  name="zhangsan"
  __age=20

  def fun1(self):
    print('aaa')
  def __fun2(self):
    print('fun2')

d = D()

print(hasattr(d, 'name')) # True
print(hasattr(d, '__age')) # False 私有属性
print(hasattr(d, 'fun1')) # True
print(hasattr(d, '__fun2')) # False 私有方法

print('⭐️ ' * 20)

### 迭代器的使用

li = [10,20,30]
y = iter(li)

# 对数据的迭代 超出则会 异常 StopIteration
print(next(y))
print(next(y))
print(next(y))

print('⭐️ ' * 20)

### 迭代器迭代对象

class I:
  def __init__(self):
    self.x = 0
  def __next__(self):
    self.x += 1
    if self.x > 10:
      raise StopIteration
    return self.x
  def __iter__(self):
    return self

i = I()
# print(list(i))
# print(set(i))
# print(tuple(i))

for item in i:
  print(item, end='')
