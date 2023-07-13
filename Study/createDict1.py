tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict)
tinydict1 = { 'abc': 456 }
print(tinydict1)
tinydict2 = { 'abc': 123, 98.6: 37 }
print(tinydict2)

emptyDict = {}
print(emptyDict)
print("Length:", len(emptyDict))
print(type(emptyDict))

emptyDict1 = dict()
print(emptyDict1)
print("Length:", len(emptyDict1))
print(type(emptyDict1))


print("-------访问字典里的值--------")
tinydict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']: ", tinydict3['Name'])
print("tinydict['Age']: ", tinydict3['Age'])

tinydict3['Age'] = 8               # 更新 Age
tinydict3['School'] = "菜鸟教程"  # 添加信息
print ("tinydict3['Age']: ", tinydict3['Age'])
print ("tinydict3['School']: ", tinydict3['School'])


print("-------删除字典元素--------")

# del tinydict3['Name'] # 删除键 'Name'
# tinydict3.clear()     # 清空字典
# del tinydict3         # 删除字典
# print ("tinydict3['Age']: ", tinydict3['Age'])
# print ("tinydict3['School']: ", tinydict3['School'])


L = [4, 2, 25, 7777777, 100, 3, 77777777, 77777777, 77777777, 77777777]
print(L)
L.sort()
print(L)