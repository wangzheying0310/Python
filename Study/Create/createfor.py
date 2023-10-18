for item in 'Hello':
    print(item)

numbers = [43,32,55,74]
for item in numbers:
    print(item)

# 循环体不中断
for item in range(10):
    print(item)
else:
    print('For Over!')

# 循环体中断
for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print('For Over!')