# 函数
# def 函数名(参数): # 这个参数 我们也称为 形参
#     # 代码块
# 调用：
# 函数名(参数) # 调用里面的这个参数叫 实参
def fn1(a, b, c=1):
    # print(888)
    # a = 1
    # b = 2
    # print(a + b + c)
    return a + b + c


# 形参传递方式：
# 如果函数调用时，也传递了这个有默认值得形参，则默认值不生效
# 如果调用时，没有传这个有默认值的形参，则默认值就会生效
# 实参传递方式：

# 位置参数
# 把对应位置 赋值对应的形参
# fn1(1,2)

# 关键字参数
# fn1(b=1,a=2)
# fn1(b=1,a=2)

# 位置参数 和 关键字 实参的 混合使用
# 关键字和位置参数可以混合使用
# 混合使用时，位置参数要写在前面，关键字参数写后面
# 如果通过位置参数指定了，就不要在用关键字重复指定

# print(fn1(2, b=3))


# 函数的实参：
# 注意
# 函数的形参名和全局的变量名，即使一样，也没有关系
# 实参的可以传任意类型的对象
# Python解释器不会去检查实参的类型，做运算需要去注意各变量类型  -----------------------------------
# 如果实参传进来的是一个列表，那在函数中改变会影响到原来的数据，如果你


def fn2(a, b):
    res = a + b
    return res

a = 100
b = '2'
# print(fn2(a, b))


def fn3(a):
    print(1111)
    a.append(5)

    return a


a = [1,2,3,4]
print(a) # [1,2,3,4]
# 如果不想让全局的可变对象 发生改变，可以对其进行copy，然后传给函数
fn3(a.copy())
print(a) #


# fn3 和 fn3() 的区别

