print("-----------break语句----------------")
# break语句  终止循环
for item in range(10):
    if item == 3:
        break
    print(item)


# continue语句  终止本次循环，跳出本次循环继续执行
print("-----------continue语句----------------")
for item in range(10):
    if item == 3:
        continue
    print(item)