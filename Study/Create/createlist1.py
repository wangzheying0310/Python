list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[1] )
print( list[2] )
print( list[-1] )
print( list[-2] )
print( list[-3] )

print(list[0:4])
# 读取第二位
print ("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2])

# 更新列表元素
print('-------更新列表-----')
list[1]= 200
print(list)

list.append('300')
print(list)

print('-------删除列表-----')
del list[1]
print(list)

print('-------插入元素-----')
list.insert(2,90)
print(list)

print('-------替换元素-----')
list[2] = 70
print(list)

print('-------删除元素-----')
list.remove(70)
print(list)