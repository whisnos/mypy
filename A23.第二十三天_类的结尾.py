class Fruits():

    def __init__(self, color, size, shape=None, name=None):
        self.color = color
        self.size = size
        self.shape = shape
        self.name = name

    def eat(self):
        print(4*5)
        print('能吃~~')

    def selled(self):
        print('能卖~~')


f = Fruits(color='多种颜色', size=5, shape='各种形状', name='大于5公分的水果')


class Apple(Fruits):
    def __init__(self, tian, color, size):
        self.tian = tian
        # self.color = color
        # self.size = size
        # Fruits.__init__(self, color, size)
        super(Apple, self).__init__(color, size)

    def eat(self):
        print('苹果能吃~~而且非常甜', self.color)
        super(Apple, self).eat()

# a = Apple(color='红色', size=10, shape='圆形', name='苹果apple')
# a.eat()
# a1 = Apple(color='绿色', size=8, shape='圆形', name='绿色的苹果apple')

a2 = Apple('非常甜', color='红色', size=10)
a2.eat()

class Banana(Fruits,):
    pass

# issubclass(a,b) 查看a，是否是b的子类
print(issubclass(Apple, Fruits))
print(issubclass(Banana, Fruits))


class A():
    a = 10
    def __init__(self, name):
        self.name = name

class B():
    def __init__(self, name):
        self.name = name

a = A('猪八戒')
b = B('孙悟空')

def say_hello(obj):
    print(f'你好，我是{obj.name}')

say_hello(a)
say_hello(b)

# 关于这个 obj，



class Apple():

    a = 1
    @classmethod
    def color(cls):
        print('color1')

    def size(self):
        print('color2')

    @staticmethod
    def shape():
        print('shape')

a = Apple()
# print(a.color())
# print(a.size())
# print(a.shape())

# 实例对象 都可以调用

print(Apple().color())
print(Apple().size())
print(Apple().shape())

'''
在class内定义的类方法（color），它第一个参数必须是cls，并与class本身是绑定关系，它也属于方法，但不属于实例方法，可以被实例对象调用。
在class内定义的普通方法（size），因为它是要面向实例化对象的一个实例方法。
在class内定义的静态方法（shape），它与任何对象都没有联系，等同于是在class外定义的function，它属于函数。
'''

import sys
dfadfafaef = 'wurong11196747467'
print(111,sys.getrefcount(dfadfafaef)) # 2
k=a
# print(111,sys.getrefcount(z))
# List={z,2}

# del a

# 随机库
import random

print(random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
print(random.random() )             # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(random.choice('tomorrow') )   # 从序列中随机选取一个元素
print(random.choice([10,88,66]) )   # 从序列中随机选取一个元素
print(random.randrange(1,3,2) )     # 生成从1到100的间隔为2的随机整数