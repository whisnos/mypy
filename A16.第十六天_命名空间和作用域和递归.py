# from test import LoginInput1
# import test
from wron import LoginInput1


def myfun():
    '''
    我的第一个函数
    :return:
    '''
    pass
    return 1


# test.LoginInput()
# LoginInput()
# help(LoginInput1)
# help(myfun)

# 命名空间 和 作用域

def max1(s):
    d = 99
    return 1


b = 2


def myname():
    print(b)
    # b = 5
    c = 11
    a = max([1, 3, 5])
    print(a)
    print(111111111, locals())


# myname()
# locals() 获取当前作用域的命名空间
# print(locals()) # 返回的是全局的对象


# 在局部作用域 你若想用全局的变量，需要先声明 采用：global 变量 方可进行修改
a = 11
print(locals())


def fn():
    # a = 25
    b = 2
    c = 3
    global a
    goobal_scope = globals()
    print(goobal_scope, type(goobal_scope))
    # print(locals())
    # goobal_scope['a'] = 30
    # print('函数内部，a=', a)
    a = 60
    # print('函数1部，a=', goobal_scope['a'])
    return


fn()
print('全局作用域，a=', a)

'''
class Dog():
    pass

    def run(self):
        print('会跑~~~')

    def eat(self):
        print('会吃~~~')


dog = Dog()
dog.run()
dog.eat()

'''


def chengfa(m):
    q = 1
    for i in range(1, m + 1):
        q *= i
        # print(i, q)
    return q


print(chengfa(10))


def sum(m):
    a = 1
    for i in range(1, m):
        a = a * i
    return a
print(sum(11))

# 递归 函数里面调用自己
# 10*9*8*7*6....*2*1
def digui(a):
    if a == 1:
        return a
    return a*digui(a-1)

print(digui(10))
# 10*9