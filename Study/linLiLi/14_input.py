# BMI = 体重 /（身高 ** 2）
height= float(input("请输入你的身高（单位 M）："))
weight = float(input("请输入你的体重（单位 KG）："))
BMI = weight / (height ** 2)
print("你的身高是"+str(height)+","+"你的体重是"+str(weight)+","+"计算得出你的BMI是"+str(BMI))