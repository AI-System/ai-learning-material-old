# 定义父类
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getInfo(self):
    print('my name: %s; 年龄: %d'%(self.name, self.age))

# 定义子类 (派生类)
class Stu(Person):
  def __init__(self, name, age, school):
    Person.__init__(self, name, age) # 去构造父类
    self.school = school
  def getInfo(self):
    print('my name: %s；my age: %d; my school: %s'%(self.name, self.age, self.school))
  
  # 子类定义父类方法的功能
  def fun(self):
    print('fun ...')

s = Stu('Jack', 30, 'Peking')
s.getInfo()
s.fun()

print('⭐️' * 20)

class A:
  name='A_jack'
  age=10
  def fun(self):
    print('A')

class B:
  name='B_jack'
  age=15
  color='red'
  def fun(self):
    print('B')

# 继承多个，重复的继承按照第一个积累来
class C(A,B):
  pass

c = C()

c.fun() # A
print(c.name) # A_jack
print(c.age) # 10
print(c.color) # red
