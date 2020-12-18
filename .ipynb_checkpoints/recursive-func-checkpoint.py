#  递归函数的优点是 定义简单，逻辑清晰。
def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)


print(fact(10))

