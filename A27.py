import os

# 获取系统变量
# print(os.path.dirname(r'D:\home\python\A27.py'))  # 返回目录路径
# print(os.path.join('root', 'test', 'debug5.txt'))
print(os.path.abspath(__file__))
print(os.path.dirname())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
# 可以用来执行操作系统指令
os.system('dir')

# os.path 常用路径操作

# 当前目录的绝对路径
print(os.path.abspath('.'))

# 上级目录的绝对路径
print(os.path.abspath('..'))

# 当前文件的绝对路径
print(os.path.abspath(__file__))

# 去掉文件名，返回目录
print(111,os.path.dirname(os.path.abspath(__file__)))
# 返回路径 path 的目录名称。这是将 path 传入函数 split() 之后，返回的一对值中的第一个元素。
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


print(os.path.basename('/root/debug5.txt'))  # 返回文件名
print(os.path.dirname('/root/debug5.txt'))  # 返回目录路径
print(os.path.split('/root/debug5.txt'))  # 分割文件名与路径
print(os.path.join('root', 'test', 'debug5.txt'))  # 将目录和文件名合成一个路径
'''