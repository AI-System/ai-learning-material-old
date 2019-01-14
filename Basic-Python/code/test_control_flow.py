# 双向分支结构

'''
num=int(input('请输入一个成绩： '))

if num >=60:
  print('合格')
else:
  print('未通过')
'''

# 多项分支结构 if elseif else 在python中无switch语句

'''
num=int(input('请输入一个成绩： '))

if num >=90:
  print('优秀')
elif num>=75:
  print('良好')
elif num>=60:
  print('合格')
else:
  print('未通过')
'''

### 嵌套结构 (巢状结构)

num = int(input('请输入一个成绩：'))

if num >= 75:
    if num >=90:
        print('优秀')
    else:
        print('良好')
else:
    if num >= 60:
        print('合格')
    else:
        print('不合格')