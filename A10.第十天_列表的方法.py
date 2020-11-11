# 列表 [] ,切片[:]
# [开始:结束:步长]
list2 = [45, 13, 156, True, 'debug5']
print(type(list2))
# 切片会新生成一个新的列表
new_list = list2[1:3]
# print(id(list2), id(new_list))
# print(type(new_list), list2, new_list)

# id 看地址，type 看类型，value

# 切片注意：
# 跟range一样，包前不包后
# 切片后返回一个新的列表
# 如果都没有写值 [:] 从头到尾，相当于 浅拷贝
# [:3] 从0开始
# [2:] 从2开始到结束
# list2 = [45, 13, 156, True, 'debug5']
# 步长默认是1，步长为负数，具体看项目需要
# new_list = list2[:]
# print(list2,new_list)

# 步长 [开始:结束:步长]  -  [2::1]
list2 = [45, 13, 156, True, 'debug5', None, 0, 13]

new_list = list2[::2] # [::0] ValueError: slice step cannot be zero
new = [45, 13, 156, True, 'debug5', None, 0, 13]
# new[new.index('debug5')]   ------  new[4]
print(list2, new_list)
# 45 debug5

str1 = 'debug5.com'
new_str1 = str1[:3:-1] # moc.5gubed
print(new_str1)
# dbg.o
count = 0
list2 = [45, 13, 156, True, 'debug5', None, 0, 13]
for i in list2:
    print(i)
    if i == 13:
        count +=1
print('count', count)
# 方法： (无返回值)   -------- -----------------一个方法，如果没有返回值，你非要接收，则为None


# 1、求某个元素的第一个索引
# 列表.index(元素)
print(666, list2.index('debug5'))

# 2、给列表往 末尾 添加新的元素(无返回值)
# 列表.append(元素)
list2.append(777) # /əˈpend/ 添加
# print(list2)
print(list2.append(777))

# 3、给列表某个位置插入元素(无返回值)
# 列表.insert(插入当前索引之前, 元素)
list2.insert(2, 666) # /ɪnˈsɜːt/ 插入
# print(list2)

# 4、计算某个元素的个数(有返回值)
# 列表.count(元素)
num = list2.count(14)
print('13个数为：', num)

new_l = [1, 2, 'python', 4, 5, 6] # [6, 5, 4, 'python', 2, 1]
# 5、反向输出(无返回值)
# 列表.reverse()
res = new_l.reverse()
print(888, res)
print(999, new_l)

# pop(),remove(),copy(),sort(),extend()

new_l = [2, 'python', 4, 5, 6]

# in , not in
if 10 not in new_l:
    print('1在列表里面')

while 1 in new_l:
    print(123)
# 根据索引来修改元素
new_l[2] = 22
print(new_l)

'''
new_l = [2, 'python', 4, 5, 6]
需求：
把 'python' 改为 'debug5' ,不能通过索引来改
'''




