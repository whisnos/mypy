class Student():
    # 累的代码里面，可以定义变量，这个是 类变量 雷属性
    class_name = '一班'
    print(666)

    # 魔法方法 特殊方法
    def __init__(self, name, age, height):
        # print(123456, name, age, height)
        self.name = name
        self.age = age
        self.height = height

    # def __del__(self):
    #     print('我是del魔法函数', self.name)
    #     pass

    def study(self):
        print(f'我是{self.name}，我在学习~~')

    def sport(self):
        # print(f'我是{self.name}，我在运动~~')
        # print('我是%s，我在运动~~' % self.name)
        print('我是{}，我在运动~~'.format(self.name))


class Cat():
    # 类变量
    category = '波斯猫'

    def __init__(b, name, age, height):
        b.name = name
        b.age = age
        b.__height = height

    def run(c):
        print('会跑',c.name,c.__height)

    def sport(self):
        pass

    # get_ 获取身高
    @property
    def get_height(self):
        print(123123)
        return self.__height

    # set_ 设置私有属性
    def set_height(self, n):
        self.__height = n
        return self.__height
c = Cat('小花', 3, 25)
# print(c.category)
c1 = Cat('小黑', 3, 25)
# print(c1.category)
# print(c.__height)
# print(c._Cat__height)
# c.run()
# c._Cat__height = 30
# 获取身高
# height = c.get_height()
# 有一个需求，不以调用函数的形式，以属性的形式
print(c.get_height, type(c.get_height)) # <class 'method'>

height1 = c.set_height(31)
print(height1)


# @property
# 可以把函数（方法）以属性的形式访问

'''
爷爷
    - 房子
爸爸
    - 车子
你
    - 有房有车
'''
class NN():
    def __init__(self,name,home):
        self.name = name
        self.home = home

    def hua(self):
        print('奶奶化妆~~')

class YY():
    def __init__(self,name,home):
        self.name = name
        self.home = home

    def eat(self):
        print('爷爷吃饭~~')
# Y = YY('爷爷', '北京四合院')
# print(id(Y))
class BB(YY,NN):
    def __init__(self,feiji,car,name,home):
        self.feiji = feiji
        self.car = car
        self.name=name
        self.home = home
        # 如果你自己实现了 init，你还想要继承爷爷的房子
        # YY 父类名
        # YY.__init__(self, name,home)
        # 等同于下面
        # super(BB,self).__init__(name,home)
    def eat(self):
        print('爸爸吃饭~~')

B = BB( '私人飞机', '小鹏汽车','爸爸', '北京四合院')

# print(B.eat())
print(B.hua())
# print(B.home)
class Wo(BB):
    def __init__(self,name,home,car):
        self.name = name
        self.home = home
        self.car = car