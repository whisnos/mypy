'''
file_name = 'd:/python/A6.第六天_运算符.py'
size = 100
with open(file_name, 'rt', encoding='utf8') as fileobj:
    # print(fileobj.)
    # 读取文本，size是以字符为单位的
    # 读取二进制，size是以字节为单位的
    print(fileobj.read(size))

'''

dict1 = {
    'code': 0,
    'msg': 'success!',
    'data': [{"username": "kunxiong", "qq": "153454354"}, {"username": "wron", "qq": "853307553"}]
}

if dict1['code'] == 0:
    data1 = dict1['data']
    for a in data1:
        print(type(a))
        # print('qq is:', a['qq'])
else:
    print('请求失败')


def ListJishu(A):
    T = []
    i = 0
    while i <= len(A) - 1:
        if i % 2 == 1:
            T.append(A[i])
        i += 1
        continue
    return T


def text():
    c = 0
    while c < 3:
        d = 0
        a = input('请输入你的账号：')
        b = input('请输入您的密码：')
        if a == "root" and b == "123456":
            print('恭喜你，登入成功')
            break
        else:
            d += 1
            print('第%d次输入的账号密码有误，请重新输入' % d)
        c += 1
    if d == 3:
        print('登入失败')

# text()


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
