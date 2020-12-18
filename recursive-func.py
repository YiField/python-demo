#  递归函数的优点是 定义简单，逻辑清晰。
def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)


print(fact(10))


# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。

# 尾递归：函数返回的时候，调用自身本身，并且return语句不包含表达式。 【把循环看成是一种特殊的尾递归函数】

def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)


print(fact2(10))

# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017268131039072
