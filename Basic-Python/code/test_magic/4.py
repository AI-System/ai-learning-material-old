class Demo:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
    return "Demo(%d, %d)"%(self.x, self.y)
  def __add__(self, other):
    return Demo(self.x + other.x, self.y + other.y) # 返回一个实例对象

d1 = Demo(5, 8)
d2 = Demo(9, -4)

print(d1 + d2) # Demo(14, 4) 两个对象相加就会调用 __add__魔术方法