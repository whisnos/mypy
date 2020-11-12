# 集合 set
# 创建
# 使用{}来创建集合
# 如何定义空集合：
a = set()
print(type(a))
# 注意：
# 1 自带去重功能
# 2 元素无序 --- 不可通过索引来取值
# 3 集合只能存储不可变对象 bool,str,float,tuple,None
# 4 集合不能存储：list,set

D = {'key': 'value', 2: 2}
# print(type(D))

# 不可变类型：bool,str,float,tuple,None
# 可变类型：list
S = {1, 15, True, False, 'python', 2.5, (1,), None, 15}
# L = [1, 2, 3, 2]
print(type(S))
# print(S[0]) # 索引取值会报错

# 集合到底是可变还是不可变？ 倒推 集合为可变类型

for i in S:
    print(i)

# 方法：
'''
基本操作	操作功能描述
len(set)	集合长度
set.add(obj)	为集合添加元素
set.clear()	移除集合中的所有元素
set.copy()	拷贝一个集合
set.difference()	返回多个集合的差集
set.difference_update()	移除集合中的元素，该元素在指定的集合也存在。
set.discard()	删除集合中指定的元素
set.intersection()	返回集合的交集
set.intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
set.isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
set.issubset()	判断指定集合是否为该方法参数集合的子集。
set.issuperset()	判断该方法的参数集合是否为指定集合的子集
set.pop(obj)	移除指定元素
set.remove(obj)	移除指定元素
set.symmetric_difference()	返回两个集合中不重复的元素集合。
set.symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
set.union()	返回两个集合的并集
set.update()	给集合添加元素
'''

L = [1, 5, 6, 5, 1]
print(list(set(L)))

# 字典 {} dict

# 集合运算
'''
交集 &
并集 |
差集 -
异或集 ^
    获取除交集外的元素
是否子集 <=
'''
print('~' * 50)
A1 = {1, 5, 8, 11}
A2 = {1, 2, 5, 10, 15, 8}

print(A1 <= A2)
'''
序列通用操作：
in 
not in 
len()
'''

# 字典 dict Dictionary  /ˈdɪkʃənri/
# 字典不是序列，是一种新的数据结构，称为映射(mapping)
# 字典的作用和列表差不多，都是存储数据的容器
# 列表存储数据的性能很好，但是查询数据的性能很差
# 字典中每一个元素都有唯一的名字，称为键（key），
# 通过这个key可以快速的查找到元素对应的值（value），所以字典我们也称为键值对（key-value）结构
# 字典的存储性能没有列表好，但是查询效率非常快

# 创建
# 使用{}来创建

D = {'name': 'xiaoming', 'age': 18, 0: 15}
print(type(D))
print(D)
print('年龄为：', D['age'])
# print('name为：', D['height'])

# 注意：
# 1 value可以是任意对象
# 2 key只能是不可变对象 int,float,bool,str,tuple,None, 不可放：列表，集合，字典
# 3 key可以不唯一，但是后面的键如果重复，会覆盖前面的值
# 4 key如果不存在 报错 KeyError: 'height'

# 增
D1 = {'NAME': '猪八戒', 'age': 38}
D1['HEIGHT'] = 175
print(D1)
# 删
# del D1['age'] # 删key而已
# del D1  # 删对象
# D1.pop('age')
# D1.clear()
# D1.popitem() # 一般删除最后一个
# 改 直接赋值
D1['HEIGHT'] = 185
# 查 取值
D1.get('ADDRESS', '默认值') # 如果key不存在，会取后面的默认值
D1['ADDRESS'] # 如果key不存 会报错
for k, v in D1.items():
    print(k, v)

A= [{'key':12},{'key':12},{'key':12},{'key':12},{'key':12},{'key':12},{'key':12},]