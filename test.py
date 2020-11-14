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
