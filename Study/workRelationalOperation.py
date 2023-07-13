
# 小明三门成绩  百分制 小于60  0积分   60-90 1积分   大于90 2积分

subject1 = int(input("请输入学科1的成绩："))
# subject2 = int(input("请输入学科2的成绩："))
# subject3 = int(input("请输入学科3的成绩："))

sorce = 0

if(subject1 < 60):
    sorce = 0
    print(sorce)
    if(subject1 > 60 & subject1 < 90):
        sorce = 1
        print(sorce)
        if(subject1 > 90):
            sorce = 2
            print(sorce)

