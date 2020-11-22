# 1、下面哪个不是Python合法的标识符：
# A: int32      B：40stu      C：self      D：Name     E：stu_class_name
# B

# 2.下列python语句正确的是：

# A：max = x > y? x : y     B:min = x  if x < y else y     C:if( x > y)  print(x)    D:while True: pass

# B D

# 3.下列哪个语句非法：
# A：x = y = z =1     B: x =(y = z +1)    C:x, y = 1, 2    D:x += 2
z = 5
(x, y) = (1, 2)
# print(x,type(x))
a = 5
b = 95
a, b = b, a
# print(a, b)
# B

# 4.关于Python内存管理，下列说法错误的是：（）
# A. 变量不必事先声明     B: 变量无需先创建和赋值而直接使用    C: 变量无需指定类型    D：可以使用del释放资源
'''
1、 Python引入了一个机制：引用计数

2、 垃圾回收机制：当引用计数为0时，调用__del__方法
'''
# b

# 5.以下不能创建一个字典的语句是：
# A：dict1 = {}    B：dict2 = {3 ： 5}    C：dict3 = {[1,2]:"value"}    D:dict4 = {'five': 5}

# c

# 6.  is，is not, ==, =区别？
'''
is、is not，比较的是内存地址是否相等。
==，比较两个值是否相当 相等，包括数值和布尔值。
=，赋值。
'''

# 7求结果：
'''
v1 = 1 or 3    ----------- 1
v2 = 1 and 3   -----------  3 
v3 = 0 and 2 and 1   ----------- 0
v4 = 0 and 2 or 1   ----------- 1
v5 = 0 and 2 or 1 or 4   ----------- 1
v6 = 0 or False and 1   ----------- False
'''
print(4545454, 0 or 1)
v1 = 0 or print(456)
print(v1)
if 1 and 2:
    print(11111)

