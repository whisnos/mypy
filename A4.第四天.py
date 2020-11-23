#
# 赋值号 =
A = 0

# 命名规范
# 像 变量名，函数名，类名

# 1、下划线命名：
product_info = 0

# 2、帕斯卡命名法，大驼峰命名法
# 每个单词的首个字母大写，其余字母小写
ProductInfo = 0

# 数据类型
# 0 1 2 3 4 5 6  整数 --- int
# 9.9 13.65 浮点数 --- float
# '我在中国' 字符串  --- str
WoChina = '我在中国'
WoChina = "我在中国"
WoChina = '''我在中国'''
WoChina = """我在中国"""
# 真 假 布尔类型 --- bool

# 嵌套问题
WoChina = "我在中国"

MyStr = '子曰："学而时习之"'

# 占位符 %s  %f  %d
# %s
GuoJia = 80
MyStr1 = "我在中国，你在%s" % 90

# print(MyStr1)
# %f 可以进行 控制浮点个数

MyStr2 = "我考90分，你考%.2f分" % 95.16854

#

# %d 只能放数值类型(整数，浮点) 结果格式化后只取整数(不存在向上，向下取整)
'''
#  5.3 --- 向下5 向上6
import math
# 向下 --- 5
num = math.floor(5.3)
# 向上  --- 6
num1 = math.ceil(5.3)
print('-----------',num1)
'''
MyStr2 = "我考90分，你考%d分" % 95.6
print(MyStr2)



# 格式化字符串 F,f   - .format() 格式化

MyName = '坤雄'
MyAddress = '长泰'
MyAge = 25

MyInfo = f'我名字叫：{MyName},我家在：{MyAddress},我今年{MyAge}岁.'

MyInfo = '我名字叫：{},我家在：{},我今年{}岁.'.format(MyName,MyAddress,MyAge)

# print(MyInfo)

# 复制字符串
BackStr = '-'*20

# print(BackStr)

# 布尔类型 真 假
# 真
a = True
# 假
b = False

# 空值 None
c = None

d = 0.1 + 0.2
# 对浮点数进行运算，可能会得到一个不准确的结果
print('结果:', d)

num = True

print(id(MyInfo))
print(type(MyInfo))
