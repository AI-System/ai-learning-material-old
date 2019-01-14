'''
字符串类型

s='abc'
type(s) # <class 'str'>

s2='10'
type(s2) # <class 'str'>

# 在字符串中输入特殊值需要转义
s3='ab\'cd'
print(s3) # ab'cd

# 换行举例
print("asd\nfas")
# asd
# fas

# 屏蔽特殊符号 使用 r
print(r"asd\nfas") # asd\nfas

# 关于字符串下标与切片的使用
name='abcde'
print(name[-1]) # e 取倒数第一个字符
print(name[-2]) # d 取倒数第二个字符
print(name[0]) # a
print(name[1]) # b
print(name[0:3]) # abc 左闭右开 (含左不含右)
print(name*2) # abcdeabcde 使用乘号来复制字符串
print('Hello: ' + name) # Hello: abcde
'''

### 关于字符串的转移

print('aaa\\bbb') # aaa\bbb

s='hello '
w='world'
print(s+w) # hello world

name='zhangsan'
name[0] # z
name[0:5] # zhang
print('an' in name) # True
print('en' not in name) # False

print('aa\\\"bb') # aa\"bb
print(r'aa\\\"bb') # aa\\\"bb
print(R'aa\\\"bb') # aa\\\"bb

print("name: %s age: %d"%('zhangsan', 20)) # name: zhangsna age:20
print('4.56789 => %0.2f'%(4.56789)) # 4.56789 => 4.57 格式化2位

print("%X"%(255)) # FF
print("%x"%(255)) # ff

### 字符串中的内建函数

name='ZhangSan'
len(name) # 8 求长度
max(name) # n 求子母中的最大值，Z 大写 没有小写字母的大
min(name) # S 求字母中的最小值

name.lower() # zhangsan
name.upper() # ZHANGSAN

name.count('an') # 统计 'an' 在 name 中出现了几次
name.replace("San", "WuJi") # ZhnagWuJi
name.find('an') # 2 返回匹配的下标 ，找不到返回 -1 【常用】
name.rfind('an') # 6 返回匹配的下标 从右侧开始查找 ，找不到返回 -1
name.index('an') # 2 返回匹配的下标 ，但是index有个问题，如果找不到会报错

s="10:20:30:40"
s.replace(":", "@") # 10@20@30#40 替换
s.split(":") # ['10', '20', '30', '40] 分割

ss=' abc '
len(ss) # 5
len(ss.strip()) # 3 去除多余的字符
