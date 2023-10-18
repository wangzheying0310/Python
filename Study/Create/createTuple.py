
# 元组（tuple）是一种不可变序列类型

tup1 = ('Google', 'Runoob', 1997, 2000)
print(tup1)
print ("tup1[0]: ", tup1[0])

tup2 = (1, 2, 3, 4, 5 )
print(tup2)
print ("tup2[1:5]: ", tup2[1:5])

tup3 = "a", "b", "c", "d"   #  不需要括号也可以
type(tup3)
print(tup3)

tup4 = ()
print(tup4)

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
print("------修改元组------")
tup5 = (12, 34.56)
tup6 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup7 = tup5 + tup6
print(tup7)

# print("------删除元组------")
# del tup1
# print ("删除后的元组 tup : ")
# print (tup1)

print("------元组索引，截取------")
print("读取第二个元素",tup1[1])
print("反向读取，读取倒数第二个元素",tup1[-2])
print("截取元素，从第二个开始后的所有元素。",tup1[1:])
print("截取元素，从第二个开始到第四个元素",tup1[1:4])

print("------元组内置函数------")
print("个数",len(tup7))
print("返回元组中元素最大值",	max(tup5))
print("返回元组中元素最小值",	min(tup5))
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print("将可迭代系列转换为元组",	tuple1)
print(id(tup1),id(tup5))

print("------拆包、打包------")
sid,sname = (102,"zhangsan")
print(sid)
print(sname)




