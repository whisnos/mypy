# 2的版本 默认ASCII，
# coding = utf8
# 对象


A = 'hello'
B = 'hello'
B = 'word'
B = A
# print(id(A))
# print(id(B))

# 类型转换 int,float,str,bool,None

# int
# 布尔转换
a = int()
# print(a) 如果没有传值 默认为0

# True --1, False --0
b = int(True)
# print(b, type(b)) # 1 <class 'int'>

b = int(False)
# print(b, type(b)) # 0 <class 'int'>

# 浮点数 - float

b = int(13.64) # 直接取整，不进行四舍五入
print(b, type(b))

# 字符串 - str

# b = int('') # int，可以转字符串的整数， 不能转字符串的浮点数 如：'15.156'，try
# print(b)

# None  - NoneType
# b = int(None)
# print(b)

# 浮点数字符串，int() 会报错
# int(None) 报错
# int('')报错


# float转换  - 把对象转成float
f = float()
print(f)
# int
f = float(25.15)
print(f)

# bool True False
f = float(True)
print(f)

f = float(False)
print(f)

# str
f = float(True) # float 不能转 空字符串，None, 字符串非数值类型，会报错
print(f)

# str  把这个对象转换成字符串
s = str(None)  # "None"
s = str(True)  # "True"
s = str(False) # "False"
s = str(20.5)  # "20.5"

print(s,type(s))

# bool 转换
b = bool(None)
print(55555555555555,b,type(b))

# 运算符
# 1 算数运算符
# ①+ 加法运算，字符串是拼接
print(float('0.1')+float('0.2'))
# ② - 减法运算，字符串不可相减 print('5'-'6')

# ③ * 乘法运算，字符串与数字相乘，复制操作。
print(25.96*20)
# ④/ 除法运算，结果返回浮点型。0不可做字母
print(4/2.8)
# ⑤// 除法运算，结果返回整数位
print(4//2.8)
# ⑥** 幂运算，
# ⑦% 取模运算，两个数相除的余数。
print(3%8)