# 1、简述解释型和编译型编程语言
# 解释型:解释器 逐行 解释成 二进制 运行
# 编译型:编译器 全部编译好 执行速度快

# 2、Python解释器种类以及特点
# CPython:
# Cpython，这个解释器是用C语言开发的，所以叫CPython，
# 在命名行下运行python，就是启动CPython解释器，CPython是使用最广的Python解释器。
#
# IPython:
# IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，
# 但是执行Python代码的功能和CPython是完全一样的，好比很多国产浏览器虽然外观不同，但内核其实是调用了IE。
#
# PyPy:
# PyPy是另一个Python解释器，它的目标是执行速度，
# PyPy采用JIT技术，对Python代码进行动态编译，所以可以显著提高Python代码的执行速度。
#
# Jython:
# Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
#
# IronPython:
# IronPython和Jython类似，只不过IronPython是运行
# 在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

# 3、如果判断自己用的是哪一种解释器？
# >>> import sys
# >>> sys.version
'3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]'

# try:
#     from platform import python_implementation
# except ImportError: # pragma: no cover
#     def python_implementation():
#         """Return a string identifying the Python implementation."""
#         if 'PyPy' in sys.version:
#             return 'PyPy'
#         if os.name == 'java':
#             return 'Jython'
#         if sys.version.startswith('IronPython'):
#             return 'IronPython'
#         return 'CPython'

# 4、位和字节的关系？
'''
	bit 位 也叫比特位 计算机最小单位 - 简单来说一位就是一个二进制数
	byte 字节 计算机操作的最小单位 8bit=1byte
'''
# 5、什么是PEP?
# Python Enhancement Proposal ， Python 增强建议书
# 一种编码规范，是为了让代码“更好看”
# https://www.python.org/dev/peps/pep-0008/
# https://python.freelycode.com/contribution/detail/47

# 6、请至少列举5个 PEP8 规范（越多越好）。

# 7、求几个结果 and or
# or 找到 真 才停
#
print(0 or '')  # 1
print(1 or 2)  # 1
print(0 and 1)  # 0
print(1 and 0)  # 0
print(0 and 2 or 1)  # 1
print(0 and 2 or 1 or 4)
print(0 or False and 1)
(0 and print(123456))  # 1
print(1 and None)  # None

if 0 and 2 or 1 or 4:
    pass

# 8、pass作用
# 1、空语句 do nothing
# 2、保证格式完整，保证语义完整
# 3、占位语句

# 9、break,continue
#
a = 0
# while a <= 10:
#     pass
#     if a == 3:
#         continue
#     print(123)
#     a += 1

# 9、is和==的区别
# is 是id比较
# == 是值比较

# 10、

'''
输入一个正常的数值年龄，输出这个人对应的人生阶段
0～17岁      少年期
18～24岁     青年期
25～44岁     壮年期
44～90岁     老年期
其他		 请输入正常年龄
'''

'''
考逻辑运算符 and or
情景：办理贷款

第一题：
	输入一个问题：你本人去办理吗？输入（去或不去）
	再输入一个问题：你老伴去吗？选择（去或不去）

	只需要有一个人去就可以办理：满足条件的话，输出："恭喜，办理成功！"
	否则都不去的话，输出："抱歉，无法办理！"
	
q1=int(inpute("你本人去办理吗？1/去，0/不去"))
q2=int(inpute("你老伴去办理吗？1/去，0/不去"))
if q1!=1 and q2!=1
   print("抱歉无法办理")
else
   print("恭喜，办理成功")
'''
you = input('你本人去办理吗？输入（去或不去）')
your = input('你老伴去吗？选择（去或不去）')

if you == '去' or your == '去':
    print("恭喜，办理成功")
else:
    print("抱歉，无法办理")
'''
练习题：

1、数值交换方法
a = 5 , b = 100

进行交换后：a 为 100，b 为5

2、如何查看系统关键字

3、三种格式化写法输出：我叫XX，我的家乡是XX，我从事XX工作。

4、列举布尔值为False的常见值？

5、求结果：
a. 1 or 2
b. 1 and 2
c. 1 < (2==2)
d. 1 < 2 == 2
'''

print(1 or 3) # 1
1 and 3 # 3
0 and 2 and 1 # 0
0 and 2 or 1 # 1
0 and 2 or 1 or 4 # 1
0 or False and 1 # False