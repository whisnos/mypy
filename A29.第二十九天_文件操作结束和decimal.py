'''
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
'''
import os
import time

# file_obj = open(file='./A666.py',mode='r+', encoding='utf-8')
# # file_obj = open(file='55.jpg', mode='rb')
# # print(file_obj,type(file_obj))
# cont = file_obj.read()
# file_obj.close()

# c = file_obj.read()
# file_obj.close()

# with open() as f:
#   f.read()
try:
    with open(file='./A666.py',mode='r+', encoding='utf8') as fileobj:
        # print(fileobj.)
        # 读取文本，size是以字符为单位的
        # 读取二进制，size是以字节为单位的
        print('with 语句代码块执行中~~')
        # read 一下子全部读取，但是你可以输入数值对读取的字符进行控制
        while True:
            cont = fileobj.read(1024)
            print(cont)
            if not cont:
                print('没内容了~~')
                break

        # readline 按行读取
        # while True:
        #     cont = fileobj.readline()
        #     print(cont)
        #     # time.sleep(5)
        #     if not cont:
        #         print('没内容了~~')
        #         break

        # readlines 全部读取，返回一个列表类型
        # while True:
        #     cont = fileobj.readlines()
        #     print(len(cont), cont)
        #     for i in cont:
        #         print(i)
        #     # time.sleep(5)
        #     if not cont:
        #         print('没内容了~~')
        #         break
except:
    print('文件不存在')
# print(fileobj.read())

# c = file_obj.read()
# file_obj.close()
# file_w_obj = open(file='66.png', mode='wb')

# file_obj.write('1234567')

# 斜杠 正斜杠 / ，反斜杠 \ - 转义符合 \t
r'''
windows是正/ 反\都可以作为路径访问

    "\"为字符串中的特殊字符，加上r后变为原始字符串，则不会对字符串中的"\t"、"\r"        进行字符串转义
    如果文件路径比较远，可以用绝对路径，用r，变为原始字符串
        file =r'C:\Users\Administrator\Desktop\tmll.out'

但是Linux下路径是用/来分割
'''
from decimal import Decimal
# getcontext().prec = 2
# print(1/7)
the_type = (Decimal(str(0.1))+Decimal(str(0.2)))
print(type(str(the_type)), str(the_type)) # .quantize(Decimal('0.0000'))
(Decimal(str(1))/Decimal(7)).quantize(Decimal('0.0000'))