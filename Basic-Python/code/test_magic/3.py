class Person:
  name='zhangsan'
  age=20

p = Person()
print(p) # <__main__.Person object at 0x10073e668>

print('⭐️ ' * 20)

class Stu:
  name='zhangsan'
  age=20

  def __str__(self):
    return "name: %s; age: %d"%(self.name, self.age)

s = Stu()
print(s) # name: zhangsan; age: 20