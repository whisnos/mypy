import json
import time
from datetime import datetime, date

'''
数值，浮点数，字符串，列表，字典，布尔，None，元组，集合，查询集
json.dumps() python数据类型--> json str
'''
n = 10
n = 10.5
n = 'debug5'
n = 'Debug5' # "Debug5"
n = [1, 2, 3, (1,)] # [1, 2, 3, [1]]
n = {'name': 'debug坤雄', 'age':18}
n = True # true
n = False # false
n = None # null
n = (1,) # [1]
n = (1, 2) # [1, 2]
n = {1, 2, 3} # TypeError: Object of type 'set' is not JSON serializable
# TypeError: Object of type 'QuerySet' is not JSON serializable
# res = json.dumps(n)

# print('res', res, type(res))

'''
def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw)
'''

n = 'debug坤雄'
res = json.dumps(n, ensure_ascii=False)
print('res', res)

# 1、ensure_ascii 是否进行ascii编码

# 2、indent
# 根据数据格式缩进显示，读起来更加清晰, indent的值，代表缩进空格式：
tup = ({'c': 'C', 'b': 'debug5官网', 'a': (1, 2, 3)})
res = json.dumps(tup, ensure_ascii=False, indent=4)
print('res', res)

# 3、separators
# 作用是可去掉',' ':' 后面的空格，在传输数据的过程中，越精简越好，冗余的东西全部去掉。
res = json.dumps(tup, ensure_ascii=False, indent=4, separators=(',', ':'))
print('res', res)

# 4、sort_keys
# 告诉编码器按照字典key排序(a到z)输出。
tup = ({'c': 'C', 'b': 'debug5官网', 'a': (1, 2, 3)})
tup = (9,5,8,'t','d')
res = json.dumps(tup, ensure_ascii=False, indent=4, sort_keys=True)
print('res', res)

# t = time.time()
t = datetime.now()
# TypeError: Object of type 'datetime' is not JSON serializable
# print(1, t)
# res = json.dumps(t)
# print('res', res)
#

# 6 cls
class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            print('datetime类型执行',obj)
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

tup = (9,5,8,'t','d', datetime.now())
res = json.dumps(tup, ensure_ascii=False, indent=4, sort_keys=True, cls=CJsonEncoder)
print('res', res)

