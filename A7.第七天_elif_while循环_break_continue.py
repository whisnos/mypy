# 期末成绩 60
# num = int(input('请输入期末成绩：'))
# if num == 100:
#     print('BMW')
# if 80 <= num <= 99:
#     print('iphone')
# if 60 <= num <= 79:
#     print('参考书')
# if num <= 60:
#     print('都没有')

# elif  60
# num = int(input('请输入期末成绩：'))
# if num == 100:
#     print('BMW')
# elif 80 <= num <= 99:
#     print('iphone')
# elif 60 <= num <= 79:
#     print('参考书')
# elif num <= 60:
#     print('xxx')
# else:
#     print('都没有')

# 判断月份是否闰年
# 什么闰年：可以被4整除且不能被100整除，或者可以被400整除
'''
num = int(input('请输入月份：'))
if num%4 == 0 and num%100 != 0 or num%400 ==0:
    print('是闰年')
# elif num%400 ==0:
#     print('是闰年')
else:
    print('不是闰年')
'''
# 循环语句
# while,for
# 注意：修改条件表达式  - 否则容易造成死循环
# while 在...什么期间
# 语法：
# while 条件表达式：
#     代码块
#
a = 1
while a:
    print('我是while循环')
    a = a - 1
print('while执行 之后')

# 注意：
# 循环的三个要素：
# 1、初始化 一个变量值
# 2、条件表达式
# 3、代码块里更新表达式，修改初始化变量


a = 0
sum = 0
flag = True
while flag:
    a += 1
    if a % 2 == 0:
        sum += a
    if a >= 100:
        # flag = False
        print('中断指令')
        break
        print(123456)
print('和为：', sum)

a = 0
sum = 0
while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1

print('和为：', sum)

# pass 占位而已 没有意义
# break 打断 - 直接整个循环结束（属于自己的范围内），直接退出循环 ----------------------------------------------------------------------
# continue 继续 - 跳过当次循环，当次continue下的代码，当次不执行，继续下一个循环--------------------------------
A = 0
while A <= 10:
    A += 1
    if A == 8:
        break
    print('666')

if 1:
    if 1:
        if 1:
            pass

# 注意：break和continue都只对最近的循环起作用

# while True:
#     print('外面')
#     while True:
#         print('里面')
#         break

num = 1
while num <= 10:
    print(num)
    if num == 3:
        continue
    num += 1

