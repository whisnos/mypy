# from fruit import sell_fruit, send_fruit, eat_fruit

# 模块名命名 遵循 标识符命名

# 导入模块的几种方法
# import 模块
'''
import fruit
print(666, fruit.A)
fruit.sell_fruit()
f = fruit.Fruit()
f.color()
'''
# import 模块 as 起别名
# from dfadf import english_game
# from dfadf import process
from dfadf import N
from dfadf import *
# print('666', N)
'''
import fruit as fr
print(666, fr.A)
fr.sell_fruit()
f = fr.Fruit()
f.color()
'''
# from 模块 import 函数，方法
'''
from fruit import send_fruit
send_fruit()
'''
# from 模块 import *  不建议使用

from tools.fruit import eat_fruit

print('xxx')

eat_fruit()

print(__name__,6666)

def A24EAT():
    print('我是A24')


# english_game()
























