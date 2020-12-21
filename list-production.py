# 列表生成式即List Comprehensions

import os
l = list(range(1, 11))
print(l)

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
l1 = range(1, 11)
print(l1)


def createDouble(l):
    l2 = []
    for x in l:
        l2.append(x*x)
    return l2


print(createDouble(l1))

# 列表生成式
print([x*x for x in l1])

# 加上if判断
print([x*x for x in l1 if x % 2 == 0])

# 两层循环，可以生成全排列
print([m*n for m in l1 for n in l1])

# 列出当前目录下的所有文件和目录名
ld = [d for d in os.listdir('.')]
print(ld)

# for循环可以同时使用两个甚至多个变量

d = {'a': '1', 'b': '2', 'c': '4'}
for k, v in d.items():
    print(k, v)


# 列表生成式也可以使用两个变量来生成list：
d2 = [k+'='+v for k, v in d.items()]
print(d2)

# 将list字符串变为小写
l = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in l])

# if进行判断 必须加上else 放在for前面
l = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(l)

# 将list进行lower()操作  str方法 int类型需进行类型转换
L = ['Hello', 'World', 18, 'Apple', None]
# l = [x.lower() if isinstance(x, str) else x for x in L]


def transform(L):
    return [x.lower() for x in L if isinstance(x, str)]
    # return [x.lower() if isinstance(x, str) else continue for x in L]


L2 = transform(L)
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
