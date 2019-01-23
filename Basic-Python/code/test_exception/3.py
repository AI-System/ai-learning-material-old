# 多处理异常
print('start')

# 存在异常的代码
try:
  # 捕获异常
  a=int(input('请输入一个数值：'))
  print('你输入的数值：', a)
  print(100 / a)
except (ValueError, ZeroDivisionError) as info:
  # 处理异常
  print('错误原因：', info)
  # raise # 再次将当前错误抛出， 但会阻塞后面的代码，后面的不会执行
except:
  print('final exept')

print('end...')
