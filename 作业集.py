# 13天
'''
1、写函数，接收两个数字参数，返回最大值
例如：
传入：10,20
返回：20

# --------------- 大宝
#第一题答题：
def max1(a=1,b=1):
    if a >= b:
        return a
    return b

print(max1(10,20))

2、写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
例如：传入：[34,23,52,352,352,3523,5]，返回：[23,352,3523]

# --------------- 大宝
#第二题答题1：
def ListJishu(A):
    T = []
    i = 0
    while i <= len(A)-1:
        if i%2 == 1:
            T.append(A[i])
        i+=1
        continue
    return T

A = [34,23,52,352,352,3523,5]
print (ListJishu(A))

#第二题答题2：
def ListJishu(A):
    return A[1::2]

A = [34,23,52,352,352,3523,5]
print (ListJishu(A))


3、写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
例如：
传入1：[34,23,52,352,666,3523,5] 返回1：[34,23,52,352,666]
传入2：[34,23,52] 返回2：[34,23,52]

# --------------- 大宝
def List5(A):
    if len(A) > 5:
        return A[:5:1]
    return A

4、写一个函数，判断用户传入的对象（字符串、列表、元组）的元素是否为空

5、写一个函数完成让用户输入用户名和密码，再写一个函数来验证这个账号和密码
如果账号为root，密码为123456，则打印出登录成功，否则继续让用户输入
账号和密码，如果三次都失败，打印登录失败

# --------------- 大宝
#登录录入函数
def LoginInput(user='',password=''):
    u = input("user:")
    p = input("password:")
    print("您已输入用户名密码！")
    return [u,p]

#登录和登录验证函数
def Login():
    i = 1
    while i <= 3:
        A = LoginInput()
        user = A[0]
        password = A[1]

        if user !='root' or password != '123456':
            i += 1
            print('用户名或密码错误')
            continue

        return print('登录成功!')
    return print('登录失败!')

Login()

'''

# 14天
'''
1、写一个函数，有一份成绩单：ScoreList = [{"name": "wron", "score": 85}, {"name": "kxion", "score": 96}, {"name": "zhihua", "score": 90}, {"name": "dabao", "score": 97}, {"name": "yujie", "score": 89}]，功能是：把分数大等于95分的学生信息返回出来；
#  ------大宝
ScoreList = [{"name": "wron", "score": 85}, {"name": "kxion", "score": 96}, {"name": "zhihua", "score": 90}, {"name": "dabao", "score": 97}, {"name": "yujie", "score": 89}]

def fenshu95(a, b=None):
    b = []
    for i in a:
        if i['score'] >= 95:
            b.append(i)
    return b

c = fenshu95(ScoreList)

2、写一个函数，功能：验证一个对象是否为整数，如果是，把值扔出来，否则做个提示告知；
def is_int(a):
    if int == type(a):
        print('是整数')
        return a
    return print('不是整数')

is_int(5)
3、写一个函数，输入一个字符串，检查字符串的长度，并检查字符串里面是否有敏感词字眼；
MINGAN = ['党','政府','公安',]
def check():
    a = input("请输入:")
    if len(a) == 0:
        return ('请不要输入空字符串')
    for i in a:
        if i in mingan:
            return ('有敏感字眼')
    return ('没有敏感字眼')

res = check()
print(res)
'''

# 15天
'''
1、写一个函数，用不定长参数来实现对数据（列表或元组）里面的数值元素，进行累加求和功能
[1,35,153,True,'debug5',None,{},(1,2),366,15,36.31]   - - - 1,35,153,366,15,36.31
（使用到 isinstance()）
'''
A=[1, 35, 153, True, 'debug5', None, {}, (1, 2), 366, 15, 36.31]
# sum = 0
def fn(*a, **kw): # 装包
    print(type(a))
    print(a)
    print(kw)
    sum = 0
    for i in a:
        if isinstance(i, (int, float)):
            sum += i
    return sum

B=fn(*A, a=66) # 拆包
print(B)







# 16天
'''
开发一个公司员工管理系统，实现对员工的管理（增，删，改，查）及退出系统

功能：
0:显示所有员工信息
1:添加一个员工信息
2:删除一个员工信息
3:修改一个员工信息
4:查询一个员工信息
exit:退出公司员工管理系统


'''



#-----------以上是函数------------



'''
开发一个公司员工管理系统，实现对员工的管理（增，删，改，查）及退出系统
功能：
0:显示所有员工信息
1:添加一个员工信息
2:删除一个员工信息
3:修改一个员工信息
4:查询一个员工信息
exit:退出公司员工管理系统'''

# 0:显示所有员工信息
def view_user():
    return user



# 1:添加一个员工信息
def add_user():
    u = input('请输入新用户名：')
    user.append(u)
    return user


# 2:删除一个员工信息
def del_user():
    u = input('请输入删除用户名：')
    if u in user:
        user.remove(u)
        return user

    del_user()  # 递归


# 3:修改一个员工信息
def change_user(j=1):
    k = j
    u = input('请输入修改的用户名：')
    for i in user:
        if i == u:
            m = input('请输入新的用户名：')
            user[user.index(i)] = m
            print('修改成功！')
            return user
    k = k + 1
    if k > 3:
        return print('输入错误次数超过3次，修改失败！')
    print('错误用户名！')
    change_user(j=k) #递归



# 4:查询一个员工信息
def select_user():
    u = input('请输入查询的用户名：')
    for i in user:
        if i == u:
            return '员工\'' + u + '\'存在'
    return '员工\'' + u + '\'不存在'

menu = '''欢迎您使用员工管理系统：
0:显示所有员工信息
1:添加一个员工信息
2:删除一个员工信息
3:修改一个员工信息
4:查询一个员工信息
exit:退出公司员工管理系统'''
print(menu)
user = ['雄雄', '宝宝', '杰杰', '华华']

def guanli():
    while True: # while 循环 条件True，一直循环。直到 break。
        v = input('请输入您需要的功能对应的序号：')
        if v == '0':
            print(view_user())
            # continue
        elif v == '1':
            add_user()
            print('添加成功！')
            # continue
        elif v == '2':
            del_user()
            print('删除成功！')
            # continue
        elif v == '3':
            change_user()
            # continue
        elif v == '4':
            print(select_user())
            # continue
        elif v == 'exit':
            print('-----------谢谢使用，再见！-------------')
            break
        # elif v not in ['0','1','2','3','4','exit']:
        #     print('错数序号！')
        #     continue
        else:
            print('错数序号！')


guanli()

'''
--------------------------------------------------------
'''
print("-" * 50, "员工管理系统", "-" * 50)

print("0:显示所有员工信息")
print("1:添加一个员工信息")
print("2:删除一个员工信息")
print("3:修改一个员工信息")
print("4:查询一个员工信息")
print("exit:退出公司员工管理系统")
list1 = ['wur']


class MyYe():
    # 0
    def xianshi(self):
        print(list1)
        return

    # 1
    def tianjia(self):
        name = str(input("输入添加员工姓名："))
        list1.append(name)
        print(name, "添加成功")
        return

    # 2
    def shanchu(self):
        name1 = str(input("输入删除员工姓名："))
        if name1 in list1:
            list1.remove(name1)
            print(name1, "删除成功")
            return
        print(name1, "不存在")

    # 3
    def xiugai(self):
        print(111)
        name3 = str(input("输入要修改的员工姓名："))
        if name3 in list1:
            name4 = str(input("修改为："))
            list1[list1.index(name3)] = name4
            print("修改成功")
        else:
            print("此员工不在公司系统")

    # 4
    def chaxun(self):
        name5 = str(input("输入要查询的员工姓名："))
        if name5 in list1:
            print(name5, "是公司员工")
        else:
            print(name5, "不是公司员工")


ye = MyYe()
while True:
    res = input("请输入：")
    if res == "0":
        ye.xianshi()
    elif res == "1":
        ye.tianjia()
    elif res == "2":
        ye.shanchu()
    elif res == "3":
        ye.xiugai()
    elif res == "4":
        ye.chaxun()
    elif res == "exit":
        break

