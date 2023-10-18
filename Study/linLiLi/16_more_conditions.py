# BMI = 体重 /（身高 ** 2）
name =input("请输入你的名字：")
height= float(input("请输入你的身高（单位 M）："))
weight = float(input("请输入你的体重（单位 KG）："))
BMI = weight / (height ** 2)
print(name + "的身高是" + str(height) + ","+ name +"的体重是" + str(weight) + "," + "计算得出的BMI是" + str(BMI))

if BMI <= 18.5:
    print("你属于偏瘦范围！")
elif 18.5 < BMI <= 25:
    print("你属于正常范围！")
elif 25 < BMI <= 30:
    print("你属于偏胖范围！")
else:
    print("你属于肥胖范围！")