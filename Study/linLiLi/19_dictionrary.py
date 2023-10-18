# 结合input、字典、if判断，做一个查询流行语含义的电子词典程序
slang_dict = {"YYDS":"永远的神"}
slang_dict["双减"] = "学生作业&校外培训双减"

query = input("请输入你想要查询的流行语：")
if query in slang_dict:
    print("您查询的" + query+ "含义如下：")
    print(slang_dict[query])
else:
    print("您查询的流行语暂未收录。")
    print("当前本词典收录的此条数为："+ str(len(slang_dict)))