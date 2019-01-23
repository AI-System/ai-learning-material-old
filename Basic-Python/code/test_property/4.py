class Rectangle:
  def __init__(self):
    self.width = 0
    self.height = 0

  def setSize(self, size):
    self.width, self.height = size # 注意：此处size可以是个元组、列表、集合

  def getSize(self):
    return self.width, self.height

  size = property(getSize, setSize) # property可以一次性处理 设置和取值

r = Rectangle()
r.size = (100, 300) # 先设置
print(r.size) # 后取值