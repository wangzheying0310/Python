shopping_list=[]
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.append("显示器")
shopping_list.append("音响")

print(shopping_list)
shopping_list.remove("键帽")
print(len(shopping_list))
print(shopping_list[1])
shopping_list[1] = "硬盘"
print(shopping_list)

price = [799,1024,200,800]
max_price = max(price)
print(max_price)
min_price = min(price)
print(min_price)
sorted_price = sorted(price)
print(sorted_price)
