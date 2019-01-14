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
