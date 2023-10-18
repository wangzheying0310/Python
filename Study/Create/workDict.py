
# 已知小红小明小亮的语文数学英语成绩，小明：85、96、88，小红：72、80、91，小亮：83、69、75
# 将姓名学科成绩做对应，计算总分最高

Chinese = {"小明":"85","小红":"72","小亮":"83"}
print(Chinese)

mathematics = {"小明":"96","小红":"80","小亮":"69"}
print(mathematics)

English = {"小明":"88","小红":"91","小亮":"75"}
print(English)

print("查询成绩")
name = input("请输入你要查询的姓名")
if name in Chinese:
    # print((name, Chinese[name]))
    print(name,"语文成绩为",(Chinese[name]))
    if name in mathematics:
        print(name, "数学成绩为", (mathematics[name]))
        if name in English:
            print(name, "英语成绩为", (English[name]))
            # 强制转换
            print(name,"总成绩为", (int(English[name]))+(int(mathematics[name]))+(int(Chinese[name])))
