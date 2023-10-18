print("素数判断器")
num = int(input("请输入一个数："))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num}不是质数！")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(f"{num}为质数！！")

else:
    print(f"{num}不是质数！")

