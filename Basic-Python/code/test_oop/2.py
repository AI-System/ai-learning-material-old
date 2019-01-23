### 类的构造方法 __init__

class A:
  def __init__(self):
    # 实例化时自动调用，一般用于初始化
    print('init ...')
  def fun(self):
    print('class A...')

a = A() # 实例化 A 时， 如果内部有 __init__ 方法, 那么会调用该方法

print('✨' * 20)

class Person:
  name=""
  age=0
  def __init__(self):
    pass
  
  def getInfo(self):
    print(self.name, " : ", self.age)

p = Person()
# 初始化之后设置参数
p.name = 'lisi'
p.age = 20
p.getInfo() 

print('✨' * 20)

class Dog:
  name=""
  age=0
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def getName(self):
    # 注意这里的第一个参数都是self
    print('test dog : name %s; age %d'%(self.name, self.age))

d = Dog('Jack', 10) # test dog : name Jack; age 10
d.getName()