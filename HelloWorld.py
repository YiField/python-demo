print("hello world")

names = ["michael", "bob", "tracy"]
sources = [95, 75, 85]
print(names)
# python函数
print(abs(-29))
print(max(-20, 9))
print(int('123'))  # 123
#print(int('123.2')) --err
print(int(123.23))
print(float('12.32'))
print(float(12))

print(str(1.23))
print(str('1.234'))
print(bool(1))

# 将整数转换成十六进制
n1 = 122
n2 = 1000
print(hex(n1))
print(hex(n2))

# 自定义函数


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-9999))

# 函数可变参数
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代
# 位置参数


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(9, 3))
print('------------')
# 默认参数


def power2(x, n=2):  # 必选参数在前，默认参数在后
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power2(33))
print('------------')

# 制定默认值


def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('sarah', 'f')
enroll('bob', 'm', city='guangzhou')

# 定义默认参数要牢记一点：默认参数必须指向不变对象！


def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end())
print('可变参数----')
# 可变参数


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
# 使用可变参数  调用该函数时，可以传入任意个参数，包括0个参数

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。[]


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc2(1, 3, 4, 2, 5))

print(calc2(*[1, 3, 2, 4]))

print('关键字参数------')

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict {}


def person(name, age, **kw):  # kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
    print('name:', name, 'age:', age, 'other:', kw)


person('michael', 30)
person('lala', 33, city="beijing")
person('haha', 333, gender="g", job="s")

# 检查关键字参数


def person2(name, age, **kw):
    if 'city' in kw:
        print('yes')
        pass
    if 'job' in kw:
        print('yes')
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person2('haha', 333, gender="g", job="s")

print('命名关键字参数------------')
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# *后面的参数被视为命名关键字参数

def person3(name, age, *, city, job):
    print(name, age, city, job)

print(person3('jacl',24,city='beijing',job='engineer'))

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888