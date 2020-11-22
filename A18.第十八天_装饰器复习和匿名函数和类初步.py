import time


def out(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        print('开始', start_time)
        s = func(*args, **kwargs)
        end_time = time.time()
        print('结束', end_time)
        print('该函数耗时为：', end_time - start_time)
        return s

    return inner


@out
def sum1():
    sum = 0
    for i in range(100000000):
        sum += i
    print('我是sum1函数', sum)
    return sum


@out
def sum2():
    sum = 1
    for i in range(1, 10000):
        sum *= i
    print('我是sum1函数', sum)
    return sum


@out
def justp():
    print('我是justp函数')
    return 'justp'


# 再写一个闭包（1函数要嵌套函数 2把第一个函数，当做参数传进去，并进行调用 3要把里面的函数return出来）


@out
def say_hello():
    print('hello')


# out(say_hello)()
# say_hello()
# sum2()
# res = out(sum1)(1, 2)
# print(111, res)
# out(sum1) # 等同于 inner

# return

# out(sum1)()  # 等同于 inner(1, 3)

# # 匿名函数：
# 语法：
# lambda 参数:返回值

def fun(x):
    return x * 10


# print(fun(2)) #10

s = lambda a, b: (a + b) * 10

# print(type(s), s(4, 4))

# filter()
'''
filter(function, iterable) 
Construct an iterator from those elements of iterable for which function returns true. 
iterable may be either a sequence, a container which supports iteration, or an iterator. 
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
'''

# def mul():
#     for i in range(10):
#         if i % 3:
#             print(i)
# mul()

res = filter(lambda x: x % 3, range(10))

# print(type(res), tuple(res))
# map() ,从可迭代的序列中，拿取每一个元素，做函数的参数，返回每一个参数的返回值，
res = map(lambda x: x +100 , range(10))

# print(type(res), tuple(res))
A = ['debug5', [13, 15], [366, 15, 36.31]]
'''

print(666, id(A))
# list.sort() 没有返回值
res = A.sort(key=len, reverse=True)
print(111, id(res), res)
print(666, id(A), A)
'''

def index(x):
    return A.index(x)

new_list = sorted(A, key=len, reverse=False)

# print(new_list)


def wrapper_out1(func):
    print('--out11--')

    def inner1(*args, **kwargs):
        print("--in11--")
        ret = func(*args, **kwargs)
        print("--in12--")
        return ret

    print("--out12--")
    return inner1


def wrapper_out2(func):
    print('--out21--')

    def inner2(*args, **kwargs):
        print("--in21--")
        ret = func(*args, **kwargs)
        print("--in22--")
        return ret

    print("--out22")
    return inner2


@wrapper_out2
@wrapper_out1
def test():
    print("--test--")
    return 1 * 2

test()

class Animal():

    def sleep(A):
        print('睡觉~~~')
        return 666


    def run(self):
        print(type(self),self,id(self))
        print('会跑~~')


# print(Animal().sleep())

class Dog(Animal):
    pass

class People():
    pass

obj = Animal()

# print(issubclass(People, Animal))

obj.sleep()
obj.run()
print(666, id(obj))