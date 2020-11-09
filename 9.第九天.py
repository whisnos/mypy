# 循环语句 while,for
# for循环
# 语法如下：
# for 迭代对象 in 字符串|列表[]|元组|字典|集合：
#   代码块

# for i in 'wenjianjia':
#     print(i)
#     pass

# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# 构序列（sequence /ˈsiːkwəns/）是python中最基本的数据结
# 序列用于保存一组有序的数据，可通过 索引 来获取其位置
# 在 Python 中，序列类型包括字符串、列表、元组

# 索引  [x]
# 序列中，每个元素都有属于自己的编号（索引）。从起始元素开始，索引值从 0 开始递增
# 除此之外，Python 还支持索引值是负数，此类索引是从右向左计数，换句话说，从最后一个元素开始计数，从索引值 -1 开始，

str1 = 'python'
# 如果超出元素个数 报错 IndexError  -------------------------------------
# print(len(1)) # TypeError: object of type 'int' has no len()
# print(len(True)) # TypeError: object of type 'bool' has no len()
# print(len(15.5)) # TypeError: object of type 'float' has no len()
# print(len(None)) # TypeError: object of type 'NoneType' has no len()

# 两种方式：
# 从0开始递增 0 1 2 3 4 ....
# 从-1开始递减  -1 -2 -3 -4 ....
print(str1[-1])

# 数值不可迭代 报错 TypeError: 'int' object is not iterable
# num = 50
# for i in num:
#     print(i)

# 在 Python 中，序列类型包括字符串、列表、元组     -   字典和结合

# range
# range(stop)
# range(start, stop[, step])  # 包前面 不包后面
# for i in range(10):
#     print(i)

# 2.0版本
# ubuntu@VM-0-6-ubuntu:~$ python
# Python 2.7.15+ (default, Nov 27 2018, 23:36:35)
# [GCC 7.3.0] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> a = range(10)
# >>> a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> type(a)
# <type 'list'>

# 3.0版本
# ubuntu@VM-0-6-ubuntu:~$ python3
# Python 3.6.9 (default, Nov  7 2019, 10:44:02)
# [GCC 8.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a = range(10)
# >>> a
# range(0, 10)
# >>> type(a)
# <class 'range'>

# 求2到100的累加求和
sum = 0
for i in range(2, 101):
    # sum = sum + i
    sum += i
print(sum)

# 求2到100的偶数累加求和 包括2和100  -  2 4 6 ....100 累加

# 唐僧大战白骨精：
# print('=' * 20, '欢迎进入游戏', '=' * 20)
# print('请选择你的身份：')
# print('     1、唐僧')
# print('     2、白骨精')
# shengm = 2
# boss = 10
# num = int(input('请选择（1-2）：'))
# if (num) == 1:
#     print('恭喜唐僧,你的生命力为2')
# elif num == 2:
#     print('白骨精，真不要脸，系统自动给你分配为唐僧！')
# else:
#     print('请不要乱输入！')
# while True:
#     print('请选择你要操作的选项：')
#     print('     1、练级')
#     print('     2、打BOSS')
#     print('     3、逃跑')
#     choice = int(input('请选择（1-3）：'))
#     if (choice) == 1:
#         shengm += 2
#         print('练级成功,你的生命力为 ', shengm)
#     elif choice == 2:
#         boss -= 2
#         shengm -= 4
#         print('攻击boss成功，boss生命力为 ', boss)
#         print('主人你生命力为 ', shengm)
#     else:
#         print('请不要乱输入！')
#     if boss <= 0:
#         print('boss挂掉了，game over')
#         break
#     if shengm <= 0:
#         print('主人你挂掉了，game over')
#         break
#

# 第十三节：数据结构
# 数据结构是指计算机中存储数据的方式 : str,int,float,bool,None,
# 列表 list [1,2,False,'python',obj...] - 大众称为 数组
for i in [1,2,False,'python']:
    print(i)

list1 = [1, 2, False, 'python']
print(type(list1), list1[-1])

# 列表，可以存储多个有序的数据
# 列表中存储的数据，我们称为元素

print([1,'字符串',True,None,[1,2,3],print])

# len() 只有可被迭代才会有len()
# print(len(1)) # TypeError: object of type 'int' has no len()
# print(len(True)) # TypeError: object of type 'bool' has no len()
# print(len(15.5)) # TypeError: object of type 'float' has no len()
# print(len(None)) # TypeError: object of type 'NoneType' has no len()

# len() 方法返回对象（字符、列表、元组、字典、集合等）长度或项目个数。
print(len('python'))
