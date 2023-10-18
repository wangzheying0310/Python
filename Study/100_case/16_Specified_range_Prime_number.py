lower = int(input("输入范围的下限："))
upper = int(input("输入范围的上限："))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # print(f"{num}不是质数！")
                # print(i, "乘于", num // i, "是", num)
                break
        else:
            print(f"{num}为质数！！")