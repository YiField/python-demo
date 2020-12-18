from collections import Iterable
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n+2

# print(L, n)
# 取List前一半元素

# list和tuple切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(L[0:3])  # 从索引0开始取，直到索引3为止，但不包括索引3。 第一位省略默认从0开始
print(L)

# 倒数切片
print(L[-2:])  # ['Bob', 'Jack']
print(L[-2:-1])  # ['Bob']

L = list(range(100))
# print(L)
# 前10个数，每两个取一个：
print(L[:10:2])

# 所有数，每5个取一个：
print(L[::5])

# 复制一个list
# print(L[:])

# tuple 的切片操作
T = tuple(range(1, 6))
print(T)
print(T[:3])

# 字符串的切片
print('ABCEDFG'[:3])
print('ABCEDFG'[::2])

# strip()
# 方法用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列。
#  注意:该方法只能删除开头或是结尾的字符,不能删除中间部分的字符。

# 编写trim()方法实现去掉字符串首尾空格


def trim(s):
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s

# 测试代码:


if trim('hello  ') == 'hello':

    print('测试成功1!')

if trim('  hello') == 'hello':

    print('测试成功2')

if trim('  hello  ') == 'hello':

    print('测试成功3')

if trim('  hello  world  ') == 'hello  world':

    print('测试成功4')

if trim('') == '':

    print('测试成功5')

if trim('    ') == '':

    print('测试成功6')

# 迭代：循环来遍历 list或tuple
list = [range(10, 20)]

d = {
    'a': 1,
    'b': 2,
    'c': 3
}
# 默认情况下，dict迭代的是key
# for key in d:
#     print(key, d[key])

# 如果要迭代value，可以用for value in d.values()
for value in d.values():
    print(value)

# 如果要同时迭代key和value
for k, v in d.items():
    print(k, v)

# 字符串迭代
for ch in 'ABC':
    print(ch)

# 通过collections模块的Iterable类型判断 一个可迭代对象
print(isinstance('abc', Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


print(L)

# 练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：


def findMinAndMax(L):
    if len(L) == 0:
        return(None, None)
    else:
        max = min = L[0]
        for d in L:
            if max < d:
                max = d
                continue
            if min > d:
                min = d
                continue
        return (min, max)


# print(findMinAndMax(L))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
