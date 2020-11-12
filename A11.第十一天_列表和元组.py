import copy
# python 浅拷贝和深拷贝
'''
浅拷贝：copy
list2 = [45, 13, 156, True, 'debug5', None, 0, 13]
'''


# n1 = 5
# n2 = 6
# print(id(n1), id(n2))



# 可变和不可变类型：
# 目前学的不可变类型：str,int,float,bool,None
# 目前学的可变类型：list,
str1 = 'debug5'
str1 = 'pebug5'
# list4 = [1,2,3,4,5]
# list4[0] = 9
# print(list4)
# str1[0] = 'p' # 字符串是不可变类型，值不可通过索引来改变，否则报错 TypeError: 'str' object does not support item assignment
# print(str1)

# print(id(list1), id(list2))

list1 = [45, 13, 156, [3, 4], 0, 13]
list2 = [45, 13, 156, [3, 4], 0, 13]

# list2 = list1.copy()
#
# print(id(list1[-1]), id(list2[-1]))
# print(list1, list2)

# 浅拷贝
list3 = [45, 13, 156, [3, 4], 0, 13]

# 浅拷贝
'''
浅拷贝，只拷贝了第一层，也就是旧的第一层改变，不会影响到新的；但是如果存在第二层及以上，其旧数据第二层改变，会影响到新的列表，因为
第二层及以上还是引用，没有拷贝，深拷贝，则都不影响
'''
list4 = list3.copy()
# 深拷贝
# list4 = copy.deepcopy(list3)

list3.append(14)
# list3[3].append(5)
print('list3', list3)
print('list4', list4)

# 百度# pop(),remove(),copy(),sort(),extend()
# 移出索引所对的元素，不写索引，默认是移出最后一个
# 列表.pop(索引)(有返回值，值为 弹出的那个元素)
l1 = [1, 2, 3, 4, 'python', [3, 4]]
# r1 = l1.pop()
# print(r1)
# print(l1)

# 移出列表中的第一个匹配元素
# 列表.remove(元素)（没有返回值）
# 如果移出不存在的元素，会报错 ValueError: list.remove(x): x not in list
# r1 = l1.remove(5)
# print(r1)
# print(l1)
n = 'python'
# if n in l1:
#     l1.remove(n)
#
# print(l1)

# 列表.copy() 其实就是浅拷贝
l2 = l1.copy()
l1[-1].append(5)
print('l1', l1)
print('l2', l2)

l1 = [1, 342, 3, 123, 12, 454]
# 列表.sort()(没有返回值)
# 注意 确保 数值不要和字符串进行比较，否则报错
# list.sort( key=None, reverse=False)
# reverse 来控制 升序 降序
# r2 = l1.sort(reverse=True)
# print(r2)
# print(l1)

# 列表.extend(值) # 值需要为iterable，如 str,list
#
l1.extend([6,7,8])
del l1[1]
print(888,l1)
l1.clear()
print(666, l1)


# 增 删 改 查
# 增
l1.append(0)
l1.insert(1,5)
l1.extend('python')# 值需要为序列 不能写 int。。
# 删
l1.pop(-1) # 传索引
l1.remove(6) # 传元素
l1.clear() # 清空列表
del l1[1]# 传索引
# 改
l1[1] = 846
# 查  查索引，查元素个数，
l1.index(5)# 传元素
l1.count(5) #传元素

# 其他
# 列表反转
l1.reverse()
# 列表排序
l1.sort(reverse=False) # reverse为False 为升序，True 为降序


# s8 = 'Life is short，you need python'
# r8 = s8.replace('python','php')
# print(11111111111, r8)
# print(22222222222, s8)
#
# r9 = s8.lower()
# print(r9)

# 二、元组tuple
print('-'*50)
t = ()
t = 1, 3, 5, 6 # 当个数只有一个 需要有,符合
print(type(t)) # <class 'tuple'>

# A B 值交换
# A = 5
# B = 100
# A, B = B, A
# print(A, B)

# 解包（解构） 可以拆序列
A,*B = 'python'
'''
注意：在进行解包的时候，变量的数量要和元组的个数一致，或者也可以在变量前面加 * ,将会获取元组剩余的元素
a,b,*c=(1,2,3,4,5,6)
'''
a, *b = t
print(a,b,type(b))

# *号可否放任何地方？ - 只能放最后一个变量
# 那可以来两个 *？ - 不行

