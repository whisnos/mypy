# hasattr(obj,name) getattr(obj,name[,default]) setattr() 函数使用详解？

class A():
    a = 10

    def __init__(self, name):
        self.name = name
        self.__height = 175


a = A('猪八戒')
# print(a.__height)
# hasattr
# print(hasattr(a, 'name'))
# print(hasattr(a, 'age'))
# print(hasattr(a, 'a'))
# print(hasattr(a, '_A__height'))

# print(getattr(a, 'age','年龄属性不存在')) #
# print(setattr(a, 'age', 15))
# print(a.age)

# 关系型数据库 和 非关系型数据库
