
# 字典表示映射关系
# dict= {key1:value1,key2:value2,key3:value3}

container = {'苹果':'A','桃子':'B','香蕉':'C','梨子':'D'}
print(container)
print(container['桃子'])

# 创建字典 添加值
price = dict()
price['苹果'] = 5
price['桃子'] = 6
price['香蕉'] = 3
price['梨子'] = 4

print(price)

if '苹果' in price:
    print("苹果的价格%d"%(price['苹果']))
else:
    print("该水果不卖")

if '荔枝' in price:
    print("荔枝的价格%d"%(price['荔枝']))
else:
    print("该水果不卖")

# print(price['荔枝'])

print("今日水果价格")
for fruit in price:
    print("%s %d 元/斤"%(fruit,price[fruit]))
print("")

n = int(input('请输入购买水果的种类数量：'))

sum_price = 0

for i in range(0,n):
    fruit = input("请输入购买的水果%d的名称："%(i+1))
    num = int(input("请输入购买的水果%d的数量："%(i+1)))

    if fruit in price:
        sum_price += price[fruit] * num
    print("总价格为%d"%(sum_price))