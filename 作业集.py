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
