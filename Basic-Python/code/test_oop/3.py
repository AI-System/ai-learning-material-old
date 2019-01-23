class Person:
  name=""
  __age=10 # 私有属性
  def __init__(self, name, age):
    self.name = name
    self.__age = age
    pass
  def getInfo(self):
    # 公有方法
    pass
  def __demo(self):
    # 私有方法
    pass
  
p = Person('wangwu', 30)
# p.__age # 报错
# p.__demo() # 报错
p.getInfo() # 正常