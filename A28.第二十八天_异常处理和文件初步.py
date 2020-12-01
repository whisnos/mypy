# print(1/0) # ZeroDivisionError
# print('0' > 1) # TypeError 没传参missing 1 required
# print(a) # 未定义就使用 NameError
# RecursionError 递归错误
# list = []
# list[5] # IndexError 超出索引
dict1 = {}
# dict1['fadf'] # KeyError
'''
语法
try:
    代码块(可能出现错误的语句)
except:
    代码块(出现错误执行的语句)
else:
    代码块(没有出错要执行的语句，异常则不执行)
finally:
    print('无论是否异常，最终都会执行')
'''

# print(1/0)
# print(123)

try:
    print(1 / 1)
    print(555)
except:
    # print(123)
    print('异常了，执行这里')


# else:
#     print('没有出错要执行的语句，异常则不执行')

def fn1():
    # try:
    print(10 / 0)
    # except:
    #     print('异常了')


def fn2():
    fn1()


def fn3():
    # try:
    fn2()
    # except:
    #     print('异常了')


# fn3()
# print(1/0)
try:
    print({}[8])
    # print([][1])
# except Exception as e:
# except Exception:
#     print(333, 'Exception')
# except IndexError:
#     print(111, 'IndexError')
except KeyError:
    print(222, 'KeyError')

l = []
b = {}
try:
    pass
    # print(10 / 0)
    # print(c)
    # 1 + '2'
    # l[10]
    # b['a']
# except ZeroDivisionError:
#     print('出现了 ZeroDivisionError')
# except NameError:
#     print('出现了 NameError')
# except TypeError:
#     print('出现了 TypeError')
# except Exception as e:
#     print('未知异常', e, type(e))
# else:
#     print(2222)
finally:
    print(123)
    print('无论是否异常，最终都会执行')
print(123)

print('*' * 100)

'''
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
'''
file_obj = open(file='A24.py',mode='w+', encoding='utf-8')
# file_obj = open(file='55.jpg', mode='rb')
# print(file_obj,type(file_obj))
cont = file_obj.read()
print('内容：',cont)
# file_w_obj = open(file='66.png', mode='wb')

file_obj.write('1234567')

# 斜杠 正斜杠 / ，反斜杠 \ - 转义符合 \t
