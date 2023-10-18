try:
    num = int(input("请输入一个数字："))

    if num == 0:
        print("该数字为0")
    elif num > 0:
        print("该数为正数")
    elif num < 0:
        print("该数为负数")
except ValueError:
    print("输入的类型错误！")
