# 列表推导式
import os
import time
import sys
# sys.path.append('..')
sys.path.insert(0, '../')
print(sys.path)
import tools
from tools.utils import current_time

current_time()
# '''
# 可变序列：list、 bytearray、 array.array、 collections.deque 和
# memoryview。

# 不可变序列：tuple、 str 和 bytes。
# '''

# # 列表推导式 示例1 把一个字符串变成 Unicode 码位的列表
# def listcomps():
#     # 普通写法
#     symbols = '$¢£¥€¤'
#     codes = []
#     for symbol in symbols:
#         codes.append(ord(symbol))
#     print(codes)


# def listcomps_1():
#     # 列表推导式，可读性更好
#     symbols = '$¢£¥€¤'
#     codes = [ord(symbols) for symbols in symbols]  # 表达式内部的变量,比如symbols，都是局部作用域
#     print(codes)
#     print(symbols)
#     print('你好')


# listcomps()
# listcomps_1()
# '''
# 列表推导与 filter 和 map比较
# '''
# print('带有条件的列表表达式')
# symbols = '$¢£¥€¤'
# beyond = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
# print(beyond)

# # filter 和 map方式
# '''
# python内置函数map和filter都是对一个序列进行相应的操作，map是对每一元素做自定义的映射，filter是对序列每个元素过滤。

# '''
# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# print(beyond_ascii)

# # 使用列表推导式计算笛卡尔积
# colors = ['black', 'white']
# sizes = ['S', 'M','L']
# tshirts = [(colors, size) for color in colors for size in sizes]
# print(tshirts)

# # 生成器表达式
# # 用生成器表达式初始化元组
# symbols = '$¢£¥€¤'
# tup = tuple(ord(symbol) for symbol in symbols)      # ord()转为Unicode字符
# print(tup)      # (36, 162, 163, 165, 8364, 164)

# # 用生成器表达式初始化数组
# import array
# arr = array.array('I', (ord(symbol) for symbol in symbols))
# print(arr)      # array('I', [36, 162, 163, 165, 8364, 164])


# # 2.3 元组不仅仅是不可变的列表
# # tuple()括号表示的是元组，功能: 除了用作不可变的列表， 它还可以用于没有字段名的记录。


# # 把元组用作记录
# t = (20, 8)
# print(divmod(20, 8)) # (2, 4) Return the tuple (x//y, x%y). Invariant: div*y + mod == x.
# print(divmod(*t))

# import os 

# path, filename = os.path.split('D:\PythonPro\AFluentPython\part2数据结构\list_comprehension.py')        # os.path.split返回以路径和最后一个文件名组成的元组
# print(path +'\\'+ filename)

# # =========================================================================

