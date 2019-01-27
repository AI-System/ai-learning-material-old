# 复制图片(二进制) 和 6.py 唯一不同指出就是 读取的时候的 模式 b , 读写都要带上b

def copyFun(src, target):
  # src 是源文件 target是目标文件
  # 打开源文件
  f1 = open(src, 'rb')
  f2 = open(target, 'wb')

  # 循环读取写入
  content = f1.readline()
  while len(content) > 0:
    # print(content, end="")
    f2.write(content)
    content = f1.readline()

  # 关闭源和目标文件
  f1.close()
  f2.close()

copyFun('img/ccc.jpg', 'img/ddd.jpg')
