score = int(input("请输入你的成绩："))

if score >= 60:
    if score >= 85:
        print("你真优秀")
    else:
        print("你的成绩还可以，仍需继续努力")
else:
    print("你还需要继续努力")