# 高阶函数
l = [1, 3, 5, 45, 15, 35, 156, ]


def fn(i):
    '''求大于5'''
    if i > 5:
        return True
    else:
        return False

def fn1(i):
    '''求偶数'''
    if i % 2 == 0:
        return True
    else:
        return False

def process_data(func,l):
    new = []

    for i in l:
        if func(i):
            new.append(i)

    return new

# 高阶之一：把函数名作为参数传进去
res = process_data(fn1, l)
print(res)

# 闭包 - 函数当成返回值返回

# 闭包满足以下三个条件：
# 1嵌套在函数里面
# 2闭包中的变量含有外部函数的参数
# 3外部函数的返回值是内部函数的引用
def func1():
    def inner():
        print(123)
        pass
    return inner

s = func1()
# print(s())

def line(a,b):
    def line_inner(x):
        return a*x+b
    # print(line_inner)
    return line_inner

line1 = (line(1, 2))
print(line1(3))

# 装饰器
import time


# def deco(func):
#     start_time = time.time()
#     print('开始时间：', start_time)
#     func()
#     end_time = time.time()
#     print('结束时间：', end_time)
#     execution_time = (end_time - start_time)
#     print("花费时间： %d ms" % execution_time)

def deco(func):
    def inner():
        start_time = time.time()
        print('开始时间：', start_time)
        func()
        end_time = time.time()
        print('结束时间：', end_time)
        execution_time = (end_time - start_time)
        print("花费时间： %d ms" % execution_time)
    return inner

# @叫语法糖   @deco 等同于 deco()()
@deco
def f():
    print("调用函数")
    time.sleep(15)
    print("结束调用")


@deco
def f1():
    print("调用函数")
    time.sleep(5)
    print("结束调用")

# deco(f)
# deco(f1)

# f()
f1()