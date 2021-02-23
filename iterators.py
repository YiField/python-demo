# 直接作用于for循环的数据类型有以下几种：

# 一类是集合数据类型，如list、tuple、dict、set、str等；

# 一类是generator，包括生成器和带yield的generator function。

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

print('------------')

# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections.abc import Iterator

print(isinstance([], Iterator))  # false
print(isinstance({}, Iterator))  # false
print(isinstance('abc', Iterator))  # false
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))  # false

print('**********')

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('啊啊啊'), Iterator))
