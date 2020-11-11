# 运算符
# 1 算数运算符
# ①+ 加法运算，字符串是拼接
print(float('0.1') + float('0.2'))
# ② - 减法运算，字符串不可相减 print('5'-'6')

# ③ * 乘法运算，字符串与数字相乘，复制操作。
print(25.96 * 20)
# ④/ 除法运算，结果返回浮点型。0不可做字母
print(4 / 2.8)
# ⑤// 除法运算，结果返回整数位
print(4 // 2.8)
# ⑥** 幂运算，
# ⑦% 取模运算，两个数相除的余数。
print(3 % 8)

# 2 赋值 运算符
# ①=   -  赋值
a = 5
# ②+=
# a = 1
a += 5  # a = a + 5

# ③-=
b = 4
b -= 5  # b = b - 5
print(b)

# ④/=
c = 10
c /= 4
print(c)
# ⑤//=
c = 10
c //= 4
print(c)
# ⑥**=   a = a**3
print(2 ** 3)
# ⑦%=

# 3 比较运算符  - 2个对象进行比较运算，总会返回一个布尔值，True or False -----------------------------
a = 20
b = 21
# ① >

# ② <

# ③ ==

# ④ >=
# print(a >= b)
# ⑤ <=
# ⑥ != 不等于
# print(a != b)

# ⑦ is 比较的是id ---------------------------------------------
print(id(a))
print(id(b))
print(a is b)
# ⑧ is not 比较的是id
print(a is not b)
print('-' * 20)

# (2)几种类型比较

# ①整形浮点型比较
d = 20
e = 31.5
# print(d > e)
# ②整形浮点型 不可与字符串比较 报错 TypeError: '>' not supported between instances of 'int' and 'str'
d = 20
e = '31.5'
# print(d >= e)
# 字符串的比较是根据Unicode编码，逐位比较

print('a' < 'b')
print(ord('a'))
print(ord('b'))
# ---
print(chr(98))
#
print('哈哈哈哈哈哈', end='--------') # 默认 \n  哈哈哈哈哈哈--------哈哈哈哈哈哈
print('哈哈哈哈哈哈')

# 4 逻辑运算符 not and or   - 这个也是用来做判断的，也是返回 True or False  --------------------------------
# ① not 逻辑非  - 不是
# 1)not False
print(not False)
# 2)not True
print(not True)
# 3)not 0
print(not 0)
# 4)not 1
print(not 1)
# 5)not ‘’
print(not '0')
# 5)not None
print(not None)


# bool 进行转换为False ：'',0,None,False,  ----------------------------------
# bool True 注意：'0','None','False'
a = '0'

# if 条件表达式:
#     执行的代码块
if a:
    print(123456)

if False:
    print('hello', )

# ② and 逻辑与  -----------------------
# 1)True and True
print(True and True)
# 2)True and False
print(True and False)
# 3)False and Fasle
print(False and Fasle)
# 4)False and True
print(False and True)
a = True
b = False
if a and b:
    print(666)

# ③ or 逻辑 或
# 1)True or True
# 2)True or False
# 3)False or Fasle
# 4)False or True

if False or True:
    pass
1 or 1
1 or 0
0 or 1
0 or 0

# 5 条件运算符 , 三元表达式，三元运算符 ，三目运算符
a = 2453221
b = 2445245
if a > b:
    max1 = a
else:
    max1 = b

print(a*b if a > b else b-a)

A = 10
B = 100
C = 1054

if A > B:
    D = A
    if D > C:
        print('最大值：', D)
        if A ==1:
            pass
    else:
        print('最大值：', C)
else:
    D = B
    if D > C:
        print('最大值：', D)
    else:
        print('最大值：', C)

# print(C if C > D = (A if A > B else B) > else D)

# input()函数  ----- 返回的是 str 字符串
print('*'*50)
i = input('请输入内容：')
print(888, type(i))
# i = input('请输入内容：')
# print(i)

username = input('请输入内容：')
if username == 'xiaozhang':
    print('我是校长')

# 练习：
# 用input输入一个数值，来判断是否大于18岁，如果大于，打出 你已经成年了，否则 打出 你还未成年

# 第十二节：流程控制语句
# 两大类：
# 条件判断语句 if...else

# 循环语句

username = input('请输入数字：')
if username == 'xiaozhang':
    print('我是校长')
