print("闰年查询器！")
year = int(input("请输入你要查询的年："))
if year % 4 == 0 and year % 400 == 0:
    print(f"{year}为闰年！")
    if year % 100 != 0:
        print(f"{year}为闰年！")
else:
    print(f"{year}为平年")
