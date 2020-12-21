# 一边循环一边计算的机制 genetator

# 把一个列表生成式的[]改成()，就创建了一个generator：

l1 = [x * x for x in range(10)]
print(l1)

l2 = (x * x for x in range(4))
print(l2)
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
try:
    print(next(l2))
except StopIteration as e:
    print('Generator return value:', e.value)

# 基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fibonacciFunc(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b  # 相当于：t = (b, a + b) # t是一个tuple a = t[0] b = t[1]
        n = n+1
    return 'done'


print(fibonacciFunc(6))

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：


def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
        a, b = b, a+b
        n = n+1
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


for f in fibonacci(1):
    print(f)

# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：


def pascal(max):
    n = 0
    l = [1]
    while(n < max):
        p = []
        for i in l:
            if i == 0 or i == len(l)-1:
                p.append(i)
            else:
                p.append(i+(i-1))
        yield p
        n = n+1
    return 'ok'


for p in pascal(6):
    print(p)
