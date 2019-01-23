# 多处理异常
print('start')

# 存在异常的代码
try:
  # 捕获异常
  a=int(input('请输入一个数值：'))
  print('你输入的数值：', a)
  print(100 / a)
except ValueError:
  # 处理异常
  print('ValueError')
except ZeroDivisionError:
  print('ZeroDivisionError')
except:
  print('final exept')

print('end...')