print("一个求平均值的程序")
total = 0
count = 0
user_input = input("请输入你要计算的数字：(完成所有数字输入后，请输入Q,终止程序！)")
while user_input != "q":
    num = float(user_input)
    total = total + num
    count += 1
    user_input = input("请输入你要计算的数字：(完成所有数字输入后，请输入Q,终止程序！)")
if count == 0:
    result = 0
else:
    result = total / count
print("您输入的数字平均值为" + str(result))
