
# 集合（set）是一个无序的不重复元素序列。

print("去重：")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

if 'orange' in basket:
    print("True")
else:
    print("False")

print("------集合间的运算------")
a = set('abracadabra')
b = set('alacazam')
print("集合a中包含而集合b中不包含的元素",a-b)
print("集合a或b中包含的所有元素",a | b)
print("集合a和b中都包含了的元素",a&b)
print("不同时包含于a和b的元素",a^b)

print("------集合推导式------")
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

print("------添加元素------")
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

thisset.update({1,3})
print(thisset)
thisset.update([1, 4], [5, 6])
print(thisset)

print("------移除元素------")
thisset.remove("Taobao")
print(thisset)
# thisset.remove("Faceook") 不存在会发生错误

thisset.discard("Facebok")
print(thisset)
thisset.pop()
print(thisset)

thisset.clear()
print(thisset)