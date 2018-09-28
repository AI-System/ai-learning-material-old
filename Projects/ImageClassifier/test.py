#!/usr/bin/env python
# encoding: utf-8

import argparse

'''
# 测试1
parser = argparse.ArgumentParser()
parser.parse_args()
'''

'''
# 测试2
# positional arguments 必选参数
# 示例：
# $ python test.py wowo
# wowo

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
'''

'''
#测试3
# 示例：
# $ python test.py --verbosity 2
# Namespace(verbosity='2')
# 2
# verbosity turned on

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
        print(args) # Namespace(verbosity='2')
        print(args.verbosity) # 2
        print("verbosity turned on") # verbosity turned on

'''

'''
# 测试4 
# 无参数示例，错误：
# $ python test.py -v
# usage: test.py [-h] [-v VERBOSITY]
# test.py: error: argument -v/--verbosity: expected one argument

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
        print("verbosity turned on")
'''

'''
# 测试5
# 支持 无参数不报错，示例:
# $ python test.py -v
# verbosity turned on

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
        print("verbosity turned on")
'''

'''
# 测试6 type=int
# 正确示例：
# $ python test.py 3
# 9
# $ python test.py '31'
# 961

# 错误示例：
# $ python test.py '31a'
# usage: test.py [-h] x
# test.py: error: argument x: invalid int value: '31a'

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help="the base")
args = parser.parse_args()
answer = args.x ** 2 # 此处是开方运算
print(answer)
'''

'''
# 测试7 将参数限定在一个可选范围内
# $ python test.py 1 -v 2
# the square of 1 equals 1

# $ python test.py 1 -v 1
# 1^2 == 1

# $ python test.py 1 -v 0
# 1

# $ python test.py 1 -v 3
# usage: test.py [-h] [-v {0,1,2}] square
# test.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)

# $ python test.py 1
# 1

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square ** 2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)

'''

'''
#测试8

# $ python test.py -h
# usage: test.py [-h] [-v | -q] x y

# calculate X to the power of Y

# positional arguments:
#  x              the base
#  y              the exponent

# optional arguments:
#  -h, --help     show this help message and exit
#  -v, --verbose
#  -q, --quiet

# $ python test.py -v 2 3
# 2 to the power 3 equals 8

# $ python test.py -q 2 3
# 8

# $ python test.py 2 3
# 2^3 == 8

# 注解： -q 和 -v 是互斥的参数， 可以看出，-q和-v不出现，或仅出现一个都可以，同时出现就会报错。

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
'''


'''

# 测试9 参数默认值
# $ python test.py 2
# 2^2 == 4

# $ python test.py 2 -v 2
# the square of 2 equals 4

# $ python test.py 2 -v 0
# 4

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], default=1,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
'''