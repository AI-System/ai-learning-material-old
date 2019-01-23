class Rectangle:
  def __init__(self):
    self.width = 0
    self.height = 0

  def setSize(self, size):
    self.width, self.height = size # 注意：此处size可以是个元组、列表、集合

  def getSize(self):
    return self.width, self.height

r = Rectangle()
r.setSize({100, 200})
print(r.width, r.height) # 100 200
print(r.getSize()) # (200, 100)