import json
# dicts2 = {1: 2, "name": "age"}
#
# f = open('1.txt', 'w')
#
# json.dump(dicts2, f)
#
# f.close()
# #把dict写进file

f = open('1.txt', 'r')

content = json.load(f)

f.close()

print('content',content,type(content))