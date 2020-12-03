# with open(file='D:/text1.txt', mode='r', encoding='utf8') as fileobj1:
#     cont1 = fileobj1.read()
#     print (cont1)
#     with open(file='D:/text2.txt', mode='r+', encoding='utf8') as fileobj2:
#         cont2 = fileobj2.read()
#
#         cont2 += cont1
#         print(cont2)
#         fileobj2.write(cont2)
#         cont3 = fileobj2.read()
#         print (cont3)


if __name__ == '__main__':
    f = open('test1.txt', 'a+', encoding='utf-8')
    f.write('666666')
    cont = f.read()
    print('内容：', cont)
    f.close()
    # f1 = open('test1.txt')
    # f1_c = f1.read()
    # f1.close()
    # print(f1_c,type(f1_c))
    #
    # f2 = open('test2.txt')
    # f2_c = f2.read()
    # f2.close()
    # print(f2_c)
    #
    # f3 = open('test3.txt', 'w')
    # f3.write(f1_c+f2_c)
    # f3.close()

    # with open(file='test1.txt', mode='r', encoding='utf8') as fileobj1:
    #     cont1 = fileobj1.read()
    #     print (cont1)
    #     with open(file='test2.txt', mode='r+', encoding='utf8') as fileobj2:
    #         cont2 = fileobj2.read()
    #
    #         cont2 += cont1
    #         print(cont2)
    #         fileobj2.write(cont2)
    #         cont3 = fileobj2.read()
    #         print(cont3)

# 字符串方法
# 1、startswith(argument)  endswith() 判断以什么开头 结尾 返回布尔： True or False

path = 'https://www.baidu.com/image/123.png'
# print(path.startswith('http://'))
# print(path.endswith('.jpg'))

# 2、判断是否 纯数字 空格 字母汉子 字母数字 纯数字 返回布尔： True or False

# isdigit() 一些特殊符号的数字 ⑴ 也会返回True
# isspace() 中只包含空格，则返回 True，否则返回 False.
# isalpha() 如果字符串全部是字母 汉子组成 则返回True, 有空格也是False
# isalnum() 至少有一个字符并且所有字符都是字母或数字
# isdecimal() 检查字符串是否数字 只包含十进制数字
# isnumeric() 一些特殊符号的数字 ⑴ 也会返回True
# s6 = '9A'
s6 = '⑴'

# print(s6.isdigit())
# print(s6.isalnum())
# print(s6.isspace())
# print(s6.isalpha())
# print(s6.isdecimal())
# print(s6.isnumeric())

# 切片的使用
# [star:stop:step]

'''
step 为负数时，取的方向，是反过来的，逆序输出,数值表步长
s1='helloworld'
s1[:]从头到尾 
s1[::]从头到尾 默认从左到右 步长为1
s1[2:-1:-2] 步长为负 方向从右到左  方向相反 取不到值
s1[-1:2:-2] 步长为负 方向从右到左 
s1[::-2]
'''
s1='helloworld'

# l d
# print(s1[-1:2:-2])

# 4、拆分 split   rsplit  -  right
s= 'python debug5'
s_list = s.split() # 默认按空格\t \n \r拆
print(type(s_list))
print(s_list)
print(s[-1])

path = 'https://www.baidu.com/image/123.txt'

s_list = path.rsplit('.txt',1)
print(s_list)

# 5、找下标 截内容

# find,rfind 找索引，有返回，返回索引值
path = 'http://www.debug5.com/image/123.jpg'
# rfind() #先找到最右边/的下标，
# print(path.find('/')) #先找到最左边/的下标
# print(path.rfind('/')) #先找到最左边/的下标
firl_name = path[path.rfind('/') + 1:]
print(firl_name)
# # split()
# list1 = path.split('/')
# print(list1[len(list1) - 1])

# 6、join() 通常列表转字符串时 应用最多 可设置连接符
lists = ['志华', '坤雄', '宇杰', '大宝']
res = ''.join(lists)
print(res)

# 7、# 找字符
s = 'debug5'
# f = s.find('e')  # 返回开始的元素的下标  找不到返回-1
# print(f)
# f = s.index('p')  # 找不到报错
f = s.rfind('g5') # 找不到返回-1
print(f)

# 8、空格问题处理
# strip() lstrip() rstrip() replace(' ','')

user_name = '    adminandminbug    '
print(1, user_name, len(user_name))
# print(user_name.rstrip())
print(user_name.replace('min','max',1))
# user_name = user_name.lstrip()
# print(2, user_name, len(user_name))

# 9、replace(old,new[,count]) 返回新的字符串
print(user_name.replace('min','max',1))

new_str = 'hello worlD1'
print(new_str.upper()) # HELLO WORLD
print(new_str.capitalize())  # Hello world 符串第一个单词（不是每个单词）的首字母大写
print(new_str.lower())
print(new_str.title()) # 字符串的每个独立单词 首字母大写
s7 = 'Hello world hello kitty'
new_str = s7.swapcase() # 切换大小写
print(new_str)