# 占位符 {}
print("{},{}".format(10,20)) # 10,20 
print()
print("⭐️ " * 20)
print()
print("{1}:{0}".format(10,20)) # 20,10 注意：{}里面的数字是要format的索引
print()
print("⭐️ " * 20)
print()
print("姓名：{}, 年龄：{}".format('Jack', 20)) # 姓名：Jack, 年龄：20

# 格式化数字举例
print("{:.2f}".format(10.6789)) # 10.68 保留2位小数 
print()
print("⭐️ " * 20)
print()
# 格式化进制
print("{:b}".format(100)) # 2进制 1100100
print("{:d}".format(100)) # 10进制 100
print("{:o}".format(100)) # 8进制 144
print("{:x}".format(100)) # 16进制 64
print()
print("⭐️ " * 20)
print()
print("[{:8}, {:8}]".format(10, 20)) # 每个数值占8位，表示输出宽度 [      10,       20] 默认右对齐
print("[{:<8}, {:>8}]".format(10, 20)) # [10      ,       20] < 表示左对齐， > 表示右对齐