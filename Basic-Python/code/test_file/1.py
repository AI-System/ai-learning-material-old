# f 是io的文件流对象
f = open('./a.txt', 'r') # r 只读
content = f.read(5) # 读取5个字符, 读取之后光标会在读取的最后一个字处
print(content) # Hello
f.close() # 关闭
