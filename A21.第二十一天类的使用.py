# 类
print(type(1))
print(type(1.5))
print(type([]))
print(type(''))

print(type((1,)))

print(type({}))
print(type({'key': 'value'}))

print(type(set()))
print(type({1, 2}))
print(type(False))
print(type(None))

'''
<class 'int'>
<class 'float'>
<class 'list'>
<class 'str'>
<class 'tuple'>
<class 'dict'>
<class 'dict'>
<class 'set'>
<class 'set'>
<class 'bool'>
<class 'NoneType'>
'''
# 自定义类
# 语法：
# 类名采用大驼峰
'''
class 类名([父类]):
    代码块
'''


# name = '坤雄'
# age = 18
# height = 175


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


print(888)
s = Student('坤雄', 18, 175)
z = Student('志华', 19, 180)

z.study()

s.sport()

print(123)
# 魔法方法
# 1 __xxx__
# 2 无需调用，自己会调用，自己在什么时候调用？
# 3 它有什么功能？
# __init__
# 初始化的时候调用
# 初始化数据

# s1 = Student()


# print(s.study())
# print(s.sport())

'''
属性
'''

print('-' * 100)


class Dog():
    def __init__(b, name, age):
        b.name = name
        b.age = age
        print(888,type(b),b,id(b))

    def run(c):
        print('会跑',c.name)

d = Dog('小黄', 2)
print(666, d,type(d),id(d))
d.run()

# 第二层封装
# 私有属性： __属性名 如：__height
# 特点：
# 私有属性，只有类内部可以访问，外部无法访问
# 实际，python底层把这个私有属性改了个名字： _类名__height
class Cat():
    def __init__(b, name, age, height):
        b.name = name
        b.age = age
        b.__height = height

    def run(c):
        print('会跑',c.name,c.__height)

    def sport(self):
        pass

c = Cat('小花', 3, 165)

print(c.name)
print(c.age)
c._Cat__height = 120
print(c._Cat__height)
# c.__height = 120
# c.run()
# print(c.)