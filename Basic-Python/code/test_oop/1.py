# 定义一个人的类
class Person:
  # pass # 此处啥都不写时使用
  # 定义属性
  name='zhangsan'
  age=20
  # 定义方法
  def fun(self):
    print('fun...')
  def getInfo(self):
    print('name: ', self.name, ' age: ', self.age)
  
print(Person) # <class '__main__.Person'> # __main__ 表示在主模块下执行

# 类的实例化
p = Person()

print(p) # <__main__.Person object at 0x109fb05c0>

print('※' * 10)

# 使用
print(p.name) # zhangsan
print(p.age) # 20
p.fun() # fun...

# 尝试修改
p.name='lisi'
p.age=10

p.getInfo() # name:  lisi  age:  10
print(p.name) # lisi # 同样的效果
print(p.age) # 10 # 同样的效果
