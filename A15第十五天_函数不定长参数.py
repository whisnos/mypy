# 不定长参数
def sun(*a, **b):
    print(1, a, type(a))
    print(2, b, type(b))

    if b.get('is_len'):
        print('开始验证长度')

sun(1,2,x=25412, y=5123512, is_len=True)


def funA(a, b, *args):
    print(a)
    print(b)
    print(args)
    print(type(args))


funA(1, 2, 3, 5, 6, 7)


print('-'*50)

# 使用不定长参数传固定值,注意，b、c可省略，a不可省略
def fuzhi(a, *b, **c):
    print(a)
    print(b)
    print(c)


fuzhi(853521, 65134, 635263, 45563, 365, x=99, y=999)

# 不可
# fuzhi()


def fn(*,a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

fn(a=1,b=2,c=3)



def sun(*a, **b): # 打包的意思
    print(1, a, type(a))
    print(2, b, type(b))

    if b.get('is_len'):
        print('开始验证长度')

sun(1,2,x=25412, y=5123512, is_len=True)

print(type(1))

# isinstance(object, classinfo)

print(666, isinstance('1', int)) # if type(1) == int



def fn(a,b,c,):
    print("a=",a)
    print("b=",b)
    print("c=",c)

t=(10,20,30)

# fn(t)

# fn(t[0], t[1], t[2])
# print(*t, type(*t))
fn(*t) # 解包

d = {'a':'xiaoming','b':18, 'c':66}

print(*d) # name age love
# print(**d) # 1 (1, 2) <class 'tuple'>
fn(**d)

def myfun():
    '''
    这是我自己定义的函数
    :return:
    '''
    pass

# 文档字符串
help(myfun)