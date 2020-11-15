
# 作业
#第一题答题：
def max1(a=1,b=1):
    if a >= b:
        return a
    return b
print(type(max1()))

print(max1(10,20))

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

#第三题答题：
def List5(A):
    if len(A) > 5:
        return A[:5:1]
    return A

A = [34,23,52,352,352,3523,5]
print (List5(A))

#第四题答题：
'''写一个函数，判断用户传入的对象（字符串、列表、元组）的元素是否为空'''
def IsEmpty(A):
    if len(A) == 0:
        return print("It is empty")
    return print("It isn't empty")

IsEmpty(())

#第五题答题：
'''写一个函数完成让用户输入用户名和密码，再写一个函数来验证这个账号和密码
如果账号为root，密码为123456，则打印出登录成功，否则继续让用户输入
账号和密码，如果三次都失败，打印登录失败'''
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




a = 5

def fn1(a, b:int, c=1):
    S = 1
    print(b,type(b))
    return S

WORD = ['他妈', '习dada']

str1 = '我是标题他的'

def check(v):
    for word in v:
        print(111, word)
        if word in WORD:
            return '存在敏感词'
    return '标题正确'


res = check(str1)
print('结果：', res)




