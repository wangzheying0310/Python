num = int(input("请输入一个数："))

factorial = 1

if num < 0:
    print("负数不存在阶乘")
elif num == 0:
    print("0的阶乘为1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"{num}的阶乘为{factorial}")
