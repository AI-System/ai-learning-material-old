class Rectangle:
  def __init__(self):
    self.width = 0
    self.height = 0

  def setSize(self, size):
    self.width, self.height = size

r = Rectangle()
r.width = 100
r.height = 50
print(r.width, r.height) # 100 50