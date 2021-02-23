# 变量可以指向函数
# Python内置的求绝对值的函数abs()
print(abs(-10))

print(abs)


# map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x


# map()传入的第一个参数是f，即函数对象本身。
r = map(f, [1, 2, 3, 5])
print(list(r))

# 把这个list所有数字转为字符串：
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1, x2), x3), x4)

print('---reduce---')
# reduce实现求和
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7]))


# 将[1,2,3,4]转成1234
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4]))


# 将string转成Int
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '1234')))
print(sum([1, 2, 3, 4]))


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def arrToNum(x, y):
    return x * 10 + y


print(reduce(arrToNum, [1, 5, 9, 2]))

# 整成一个函数

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2m(s):
        return DIGITS[s]

    return reduce(fn, map(char2m, s))


# print(str2int('1232'))


# lambda 匿名函数 其后紧跟函数参数
def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int2('1232'))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     if name.length>0:
#         return name[0].upper();
#     else :
#         return ''
# print(map(normalize,['lala','jj']))
def normalize(name):
    def toUpper(n):
        if n.length > 0:
            return n[0].upper();
        else:
            return ''
    return map(toUpper,name)
print(normalize(['lid','ijl']))
