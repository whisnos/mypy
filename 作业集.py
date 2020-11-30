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


# 装饰器
'''
def zhuang(func):
    def inner(a, b):
        print('程序开始运行')
        root = input('请输入你的用户名：')
        if root == 'root' or root == 'admin':
            k = func(a, b)
            return k
        else:
            print('你输入的用户名有误')
            return False

    return inner


@zhuang
def sun(a, b):
    k = a + b
    return k


print(sun(1, 2))
'''

# 21天
# 志华 --------------------------------------------------------
'''
定义一个警察类：
 警察有名字，有血量HP，默认是1000，
 警察有一个抓人的功能，可以回血500

定义一个普通人类：
 普通人有名字，有血量HP，默认是800

定义一个小偷类：
 小偷也有名字，有血量HP，默认是200
 小偷有一个偷普通人东西的功能，可以回血250，然后普通人要掉血300


游戏顺序:
小偷去偷普通人的一个东西，
然后普通人看自己的血量
警察去抓小偷
'''


class Polic():
    def __init__(self, name1):
        self.name1 = name1
        self.hp1 = 1000

    def take(self):
        print("警察现在血量为：", self.hp1)
        print("警察开始抓小偷了")
        self.hp1 += 500
        print("警察抓到小偷了自身回血500，现在为：", self.hp1)


class People():
    def __init__(self, name2):
        self.name2 = name2
        self.hp2 = 800

    def see(self):
        while True:
            if self.hp2 >= 0:
                print("平民现在血量为：", self.hp2)
                self.hp2 -= 300
                print("平民被偷了，自身还剩:", self.hp2)
                return C.take()
            else:
                print("平民没血啦，小偷赢了")
                break


class Stolen():
    def __init__(self, name3):
        self.name3 = name3
        self.hp3 = 200

    def steel(self):
        while True:
            if self.hp3 >= 0:
                print("小偷现在血量为：", self.hp3)
                print(self.name3, "开始偷东西了")
                self.hp3 += 250
                return B.see()
            else:
                print("小偷没血啦，警察和平民赢了")
                break


A = Stolen("小偷")
B = People("平民")
C = Polic("警察")
count = 3
while count >= 0:
    print('-' * 50)
    A.steel()
    count -= 1
# 大宝的 ---------------------------------------

# 定义一个警察类：
#  警察有名字，有血量HP，默认是1000，
#  警察有一个抓人的功能，可以回血500
#
# 定义一个普通人类：
#  普通人有名字，有血量HP，默认是800
#
# 定义一个小偷类：
#  小偷也有名字，有血量HP，默认是200
#  小偷有一个偷普通人东西的功能，可以回血250，然后普通人要掉血300
#
#
# 游戏顺序:
# 小偷去偷普通人的一个东西，
# 然后普通人看自己的血量
# 警察去抓小偷
class Police:
    def __init__(self, name, blood=1000):
        self.name = name
        self.blood = blood

    def zhua(self, obj):
        self.blood += 500
        obj.blood -= 200
        print(f'{self.name}抓到小偷{obj.name},回血500,{obj.name}掉血200', self.blood, obj.blood)


class people:
    def __init__(self, name, blood=800):
        self.name = name
        self.blood = blood

    def get_caught(self, obj):
        self.blood -= 300
        obj.blood += 250
        print(f'{self.name}东西被偷了，掉血300', self.blood)


class thief:
    def __init__(self, name, blood=200):
        self.name = name
        self.blood = blood

    def tou(self, obj):
        self.blood += 250
        obj.blood -= 300
        print(f'偷到了东西，普通人掉血300，回血250', self.blood)



print('=' * 20, '欢迎进入游戏', '=' * 20)
print('请选择你的身份：')
print('     1、警察')
print('     2、普通人')
print('     3、小偷')
a = Police('警察小明')
b = people('小东')
b1 = people('小明')
c = thief('小偷高高')
num = int(input('请选择(1-3):'))
if (num) == 1:
    print(f'恭喜{a.name}，你的血量为{a.blood}')
elif (num) == 2:
    print(f'恭喜{b.name}，你的血量为{b.blood}')
elif (num) == 3:
    print(f'你是{c.name}，你的血量为{c.blood}')
else:
    print('请不要乱输入')
while True:
    print('请选择你要操作的选项：')
    print(f'     1、{a.name}抓{c.name}')
    print(f'     2、{b.name}快跑')
    print(f'     3、{c.name}偷东西')
    choice = int(input('请选择（1-3）：'))
    if (choice) == 1:
        # c.blood -= 200
        a.zhua(c)
        print('抓到小偷了')
        # break
    elif (choice) == 2:
        # b.blood -= 300
        b.get_caught(c)
        print(f'{self.name}东西被偷了')
        # break
    elif (choice) == 3:
        c.tou(b1)
        c.tou(b)
        # c.blood += 250
        # break
    else:
        print('请不要乱输入')
        # break

# 坤雄 ----------------------------------------------------
# 定义一个警察类：
#  警察有名字，有血量HP，默认是1000，
#  警察有一个抓人的功能，可以回血500
#
# 定义一个普通人类：
#  普通人有名字，有血量HP，默认是800
#
# 定义一个小偷类：
#  小偷也有名字，有血量HP，默认是200
#  小偷有一个偷普通人东西的功能，可以回血250，然后普通人要掉血300
#
#
# 游戏顺序:
# 小偷去偷普通人的一个东西，
# 然后普通人看自己的血量
# 警察去抓小偷
class Police:
    def __init__(self, name, blood=1000):
        self.name = name
        self.blood = blood

    def zhua(self, obj):
        self.blood += 500
        obj.blood -= 200
        print(f'{self.name}抓到小偷{obj.name},回血500,{obj.name}掉血200', self.blood, obj.blood)


class people:
    def __init__(self, name, blood=800):
        self.name = name
        self.blood = blood

    def get_caught(self, obj):
        self.blood -= 300
        obj.blood += 250
        print(f'{self.name}东西被偷了，掉血300', self.blood)


class thief:
    def __init__(self, name, blood=200):
        self.name = name
        self.blood = blood

    def tou(self, obj):
        self.blood += 250
        obj.blood -= 300
        print(f'偷到了东西，普通人掉血300，回血250', self.blood)



print('=' * 20, '欢迎进入游戏', '=' * 20)
print('请选择你的身份：')
print('     1、警察')
print('     2、普通人')
print('     3、小偷')
a = Police('警察小明')
b = people('小东')
b1 = people('小明')
c = thief('小偷高高')
num = int(input('请选择(1-3):'))
if (num) == 1:
    print(f'恭喜{a.name}，你的血量为{a.blood}')
elif (num) == 2:
    print(f'恭喜{b.name}，你的血量为{b.blood}')
elif (num) == 3:
    print(f'你是{c.name}，你的血量为{c.blood}')
else:
    print('请不要乱输入')
while True:
    print('请选择你要操作的选项：')
    print(f'     1、{a.name}抓{c.name}')
    print(f'     2、{b.name}快跑')
    print(f'     3、{c.name}偷东西')
    choice = int(input('请选择（1-3）：'))
    if (choice) == 1:
        # c.blood -= 200
        a.zhua(c)
        print('抓到小偷了')
        # break
    elif (choice) == 2:
        # b.blood -= 300
        b.get_caught(c)
        print(f'{self.name}东西被偷了')
        # break
    elif (choice) == 3:
        c.tou(b1)
        c.tou(b)
        # c.blood += 250
        # break
    else:
        print('请不要乱输入')
        # break

# 猜单词
# 志华
import random
def abc():
    word = ["scripts", "desktop", "finished", "exit", "code"]
    word1 = random.choice(word)
    word2 = list(word1)
    # print(word1,len(word1))
    # for n in word1:
    #     word2.append(n)
    # print(word2)
    # word4=""
    # for i in word2:
    #     word4 = word4 + i
    word5=""
    random.shuffle(word2)
    # print(word2)
    for i in word2:
        word5 = word5 + i
    print(word5)
    while True:
        word6 = input("猜猜您觉得正确的单词:")
        if word6 == word1:
            print("真棒，你猜对了。英雄请继续")
            return abc()
        else:
            print("猜错啦")
            while True:
                an = input("是否继续猜(Y/N)？")
                if an=="Y" or an=="y":
                    break
                if an == "N" or an == "n":
                    return abc()
            else:
                print("输入Y或N")
                continue
        continue
abc()

# 志华
def english_game():
    print(1111)
    words = ['hello', 'print', 'inpute', 'import', 'range', 'class', 'string', 'tuple', 'list', 'tuple', 'set']
    print("欢迎参加本次游戏，游戏规则是：\n请您猜一下打乱字母顺序的单词，如果才对可以继续游戏，\n如果猜错请继续猜！")
    while True:  # 如果是y或者Y才执行
        starGame = input('要开始游戏吗(Y/N):')
        if starGame == 'y' or starGame == 'Y':

            randomWord = random.choice(words)  #
            correctWord = randomWord  # 随机选出来的单词，因为之后要改变所有赋给correctword
            jumbleWord = ''
            while randomWord:
                position = random.randrange(len(randomWord))
                jumbleWord += randomWord[position]
                randomWord = randomWord[:position] + randomWord[(position + 1):]
            print('乱序后单词：', jumbleWord)
            guessWord = input('\n请您猜猜看：')
            while guessWord != correctWord and guessWord != '':
                print("不好意思，您猜的不正确。")
                guessWord = input("继续您猜：")
            if guessWord == correctWord:
                print("恭喜您！猜对啦！\n")
            # starGame = input("\n\n请问是否继续游戏（Y/N）:")
        else:
            print('欢迎下次再来玩')
            break