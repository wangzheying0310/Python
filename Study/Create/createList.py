# 创建集合
e = set()
f = {1,2,'abc'}
print(e)
print(f)


g = {1,2,1,1,2}
# 集合会将默认元素归一化
print(g)

# 集合是无序的，但是集合可以通过遍历来打印元素
test = {1,2,'abc',587,8}
for item in test:
    print(item)

# 增加元素
test.add(3)

print(test)
# 减少元素
test.remove(8)
print(test)

# 字符串
a = 'abcde'
test = set(a)
print(test)

# 列表
b = [1,2,3]
test = set(b)
print(test)

# 元组
c = (1,2,'abc')
test = set(c)
print(test)

# 字典
d = {'a':1,'b':2,'c':3}
test = set(d)
print(test)

# 集合运算

# 交集 取公共元素 & / intersection

# 并集 取全部元素 | / union

# 差集 取一个集合中另一个集合中没有的元素 - / difference

h = {1,2,3,4}
i = {3,4,5,6}

print(h&i)
print(h.intersection(i))

print(i&h)
print(i.intersection(h))

print(h|i)
print(h.union(i))

print(h-i)
print(h.difference(i))

num1 = int(input('请输入班级1的学生数量：'))
class1 = set()

for j in range(0,num1):
    name = input('输入学生%d姓名：'%(j+1))
    class1.add(name)

num2 = int(input('请输入班级2的学生数量：'))
class2 = set()

for j in range(0,num2):
    name = input('输入学生%d姓名：'%(j+1))
    class2.add(name)

same = class1 & class2

print("重名学生：")

for name in same:
    print(name)

print("班级2中出现但在班级1中未出现的学生姓名：", class2 - class1)



