print("请在下面输入你想要查看数字区间的乘法表！")
lower = int(input("输入范围的下限："))
upper = int(input("输入范围的上限："))
for i in range(lower, upper + 1):
    for j in range(1, i + 1):
        print('{}X{}={}\t'.format(j, i, i * j), end='')
    print()
