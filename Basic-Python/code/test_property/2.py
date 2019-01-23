class Rectangle:
  def __init__(self):
    self.width = 0
    self.height = 0

  def setSize(self, size):
    self.width, self.height = size # 注意：此处size可以是个元组、列表、集合

r = Rectangle()
# r.width = 100
# r.height = 50

# r.setSize((100, 200))
# r.setSize([100, 200])
r.setSize({100, 200})
print(r.width, r.height) # 100 200