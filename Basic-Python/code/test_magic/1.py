### 魔术方法实例

class File:
  def __init__(self, name):
    self.name = name
    print('open file', self.name)

  def __del__(self):
    print('close file', self.name)

f1 = File('a.txt')
f2 = File('b.txt')
f3 = File('c.txt')

print('hah test read & write')

'''
运行结果：
open file a.txt
open file b.txt
open file c.txt
hah test read & write
close file a.txt
close file b.txt
close file c.txt
'''